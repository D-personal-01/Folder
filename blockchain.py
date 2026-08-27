import hashlib
import json
from time import time




class blockchain:
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]

    def new_block(self):
        pass

    def new_transacction(self):
        pass

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

    
    def new_transaction(self, sender, recipient, amount):
        

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


