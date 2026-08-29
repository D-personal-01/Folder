import hashlib
guess_hash = hashlib.sha256("10035291".encode()).hexdigest()
print(guess_hash)