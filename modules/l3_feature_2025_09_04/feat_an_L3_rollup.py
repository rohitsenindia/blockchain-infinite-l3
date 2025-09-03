import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, commitment_bytes, message_bytes):
    public_key = PublicKey.fromString(public_key_bytes)
    commitment = int.from_bytes(commitment_bytes, byteorder='big')
    message = int.from_bytes(message_bytes, byteorder='big')
    r, s = proof
    R = public_key.point + public_key.point * s
    c = hashlib.sha256((str(commitment) + str(message) + str(R.x) + str(R.y)).encode()).hexdigest()
    c_int = int(c, 16)
    v = (c_int * r + message) % 2**256
    return v == commitment

proof = (12345678901234567890123456789012, 987654321098765432109876543210)
public_key_bytes = bytes.fromhex("0479BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8")
commitment_bytes = bytes.fromhex("1A2B3C4D5E6F7A8B9C0D1E2F3A4B5C6D")
message_bytes = bytes.fromhex("70617373776F7264")

is_valid = verify_zk_proof(proof, public_key_bytes, commitment_bytes, message_bytes)
print(is_valid)

