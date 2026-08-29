import hashlib


def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:6] == "000000"


def proof_of_work(last_proof):
    proof = 0

    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


# Previous proof
last_proof = 100

print("Starting Proof of Work...")
print("Previous proof:", last_proof)

# Find the correct proof
new_proof = proof_of_work(last_proof)

print("\nProof found!")
print("New proof:", new_proof)

# Show the hash
guess = f'{last_proof}{new_proof}'.encode()
guess_hash = hashlib.sha256(guess).hexdigest()

print("Hash:", guess_hash)