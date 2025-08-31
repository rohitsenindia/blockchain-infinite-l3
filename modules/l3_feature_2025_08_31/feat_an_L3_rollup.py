import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, commitment):
    public_key = PublicKey.fromBytes(public_key_bytes)
    r, s = proof
    message = commitment + public_key.toBytes()
    digest = hashlib.sha256(message).digest()
    signature = r + s
    valid = public_key.verify(signature, digest)
    return valid

proof = (b'\x01' * 32, b'\x02' * 32) # Replace with actual proof
public_key_bytes = b'\x03' * 65  #Replace with actual public key
commitment = b'\x04' * 32 # Replace with actual commitment

is_valid = verify_zk_proof(proof, public_key_bytes, commitment)
print(is_valid)
