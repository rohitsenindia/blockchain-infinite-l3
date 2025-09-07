import hashlib
from ellipticcurve.privateKey import PrivateKey

def verify_zk_proof(proof, public_key, commitment, message):
    r, s = proof
    try:
        pk = PrivateKey()
        pk.publicKey().verify(hashlib.sha256(commitment + message).digest(), (r, s))
        return True
    except Exception:
        return False


# Example usage (replace with actual proof, keys, and data)
private_key = PrivateKey()
public_key = private_key.publicKey()
message = b"This is a test message"
commitment = b"This is a test commitment"
signature = private_key.sign(hashlib.sha256(commitment + message).digest())

proof = (signature.r, signature.s)

is_valid = verify_zk_proof(proof, public_key, commitment, message)

print(is_valid)
