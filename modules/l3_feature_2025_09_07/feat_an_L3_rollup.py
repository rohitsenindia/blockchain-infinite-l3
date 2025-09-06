import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, commitment, transaction_hash):
    public_key = PublicKey.fromBytes(public_key_bytes)
    r, s = proof
    signature = public_key.sign(transaction_hash + commitment)
    return signature == (r,s)


# Example usage (replace with actual values from rollup)
private_key = PrivateKey()
public_key_bytes = private_key.publicKey().toBytes()
commitment = hashlib.sha256(b"transaction data").digest()
transaction_hash = hashlib.sha256(b"transaction hash").digest()
proof = private_key.sign(transaction_hash + commitment)

verification_result = verify_zk_proof(proof, public_key_bytes, commitment, transaction_hash)

print(verification_result)

