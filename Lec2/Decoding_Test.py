import hashlib

# Example SHA256 hash
hash_string = "7c1a4a1d4b462cb7b767e6d653440877683f11b5c1b069717c1fe75b5fc605ab"

# Convert the hash string to bytes
hash_bytes = bytes.fromhex(hash_string)

# Use the hashlib module to decode the hash
decoded_hash = hashlib.sha256(hash_bytes).hexdigest()

# Print the decoded hash
print(decoded_hash)




#7c1a4a1d4b462cb7b767e6d653440877683f11b5c1b069717c1fe75b5fc605ab