import hashlib
import json
import requests

from time import time
from uuid import uuid4
from urllib.parse import urlparse

from flask import Flask, jsonify, request


class Blockchain(object):

    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the Genesis Block
        self.new_block(previous_hash=1, proof=100)

    # ---------------------------------------------------------
    # CREATE A NEW BLOCK
    # ---------------------------------------------------------

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block and adds it to the blockchain.
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': (
                previous_hash
                if previous_hash is not None
                else self.hash(self.chain[-1])
            )
        }

        # Clear transactions after putting them into the block
        self.current_transactions = []

        # Add the block to the chain
        self.chain.append(block)

        return block

    # ---------------------------------------------------------
    # CREATE A NEW TRANSACTION
    # ---------------------------------------------------------

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of pending transactions.

        The transaction will be included in the next mined block.
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        # Return the index of the block
        # that will contain this transaction
        return self.last_block['index'] + 1

    # ---------------------------------------------------------
    # GET LAST BLOCK
    # ---------------------------------------------------------

    @property
    def last_block(self):
        """
        Returns the most recently added block.
        """

        return self.chain[-1]

    # ---------------------------------------------------------
    # HASH A BLOCK
    # ---------------------------------------------------------

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.
        """

        block_string = json.dumps(
            block,
            sort_keys=True
        ).encode()

        return hashlib.sha256(block_string).hexdigest()

    # ---------------------------------------------------------
    # PROOF OF WORK
    # ---------------------------------------------------------

    def proof_of_work(self, last_proof):
        """
        Finds a number that produces a hash
        beginning with four zeroes.
        """

        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    # ---------------------------------------------------------
    # VALIDATE PROOF
    # ---------------------------------------------------------

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Checks whether a proof is valid.
        """

        guess = f'{last_proof}{proof}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == '0000'

    # ---------------------------------------------------------
    # REGISTER NODE
    # ---------------------------------------------------------

    def register_node(self, address):
        """
        Adds another blockchain node to our list of nodes.
        """

        parsed_url = urlparse(address)

        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        else:
            raise ValueError("Invalid node address")

    # ---------------------------------------------------------
    # VALIDATE BLOCKCHAIN
    # ---------------------------------------------------------

    def valid_chain(self, chain):
        """
        Checks whether an entire blockchain is valid.
        """

        if not chain:
            return False

        last_block = chain[0]

        current_index = 1

        while current_index < len(chain):

            block = chain[current_index]

            # Check previous hash
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check Proof of Work
            if not self.valid_proof(
                last_block['proof'],
                block['proof']
            ):
                return False

            last_block = block

            current_index += 1

        return True

    # ---------------------------------------------------------
    # CONSENSUS / RESOLVE CONFLICTS
    # ---------------------------------------------------------

    def resolve_conflicts(self):
        """
        Finds the longest valid blockchain among neighbouring nodes.

        If another node has a longer valid chain,
        replace our chain with that chain.
        """

        neighbours = self.nodes

        new_chain = None

        # Current chain length
        max_length = len(self.chain)

        for node in neighbours:

            try:

                response = requests.get(
                    f'http://{node}/chain',
                    timeout=5
                )

                if response.status_code != 200:
                    continue

                data = response.json()

                length = data['length']
                chain = data['chain']

                # Replace our chain only if:
                # 1. The other chain is longer
                # 2. The other chain is valid
                if (
                    length > max_length
                    and self.valid_chain(chain)
                ):
                    max_length = length
                    new_chain = chain

            except requests.RequestException:
                # Ignore nodes that cannot be reached
                continue

        # Replace our chain
        if new_chain is not None:
            self.chain = new_chain
            return True

        return False


# =============================================================
# FLASK APPLICATION
# =============================================================

app = Flask(__name__)


# Generate a unique ID for this blockchain node
node_identifier = str(uuid4()).replace('-', '')


# Create our Blockchain
blockchain = Blockchain()


# =============================================================
# HOME
# =============================================================

@app.route('/', methods=['GET'])
def home():

    return jsonify({
        'message': 'Blockchain server is running',
        'endpoints': {
            'GET /chain': 'View the blockchain',
            'GET /mine': 'Mine a new block',
            'POST /transactions/new': 'Create a transaction',
            'POST /nodes/register': 'Register blockchain nodes',
            'GET /nodes/resolve': 'Resolve blockchain conflicts'
        }
    })


# =============================================================
# MINE A NEW BLOCK
# =============================================================

@app.route('/mine', methods=['GET'])
def mine():

    # Get the last block
    last_block = blockchain.last_block

    # Get the proof from the last block
    last_proof = last_block['proof']

    # Perform Proof of Work
    proof = blockchain.proof_of_work(last_proof)

    # Give the miner a reward
    blockchain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    # Calculate the hash of the previous block
    previous_hash = blockchain.hash(last_block)

    # Create the new block
    block = blockchain.new_block(
        proof=proof,
        previous_hash=previous_hash
    )

    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


# =============================================================
# CREATE A NEW TRANSACTION
# =============================================================

@app.route('/transactions/new', methods=['POST'])
def new_transaction():

    # Get JSON data sent by the user
    values = request.get_json()

    # Make sure JSON data was provided
    if not values:
        return jsonify({
            'error': 'Request body must contain JSON'
        }), 400

    # Required fields
    required = [
        'sender',
        'recipient',
        'amount'
    ]

    # Check whether all required fields exist
    if not all(key in values for key in required):

        return jsonify({
            'error': 'Missing required values',
            'required': required
        }), 400

    # Add the transaction
    index = blockchain.new_transaction(
        sender=values['sender'],
        recipient=values['recipient'],
        amount=values['amount']
    )

    response = {
        'message': f'Transaction will be added to Block {index}'
    }

    return jsonify(response), 201


# =============================================================
# SHOW FULL BLOCKCHAIN
# =============================================================

@app.route('/chain', methods=['GET'])
def full_chain():

    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200


# =============================================================
# REGISTER NODES
# =============================================================

@app.route('/nodes/register', methods=['POST'])
def register_nodes():

    values = request.get_json()

    if not values:
        return jsonify({
            'error': 'Request body must contain JSON'
        }), 400

    nodes = values.get('nodes')

    if nodes is None:
        return jsonify({
            'error': 'Please supply a valid list of nodes'
        }), 400

    if not isinstance(nodes, list):
        return jsonify({
            'error': 'nodes must be a list'
        }), 400

    for node in nodes:

        try:
            blockchain.register_node(node)

        except ValueError:
            return jsonify({
                'error': f'Invalid node address: {node}'
            }), 400

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes)
    }

    return jsonify(response), 201


# =============================================================
# RESOLVE CONFLICTS
# =============================================================

@app.route('/nodes/resolve', methods=['GET'])
def consensus():

    replaced = blockchain.resolve_conflicts()

    if replaced:

        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }

    else:

        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200

if __name__ == '__main__':
    import sys

    port = 5000

    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    app.run(
        host='0.0.0.0',
        port=port
    )