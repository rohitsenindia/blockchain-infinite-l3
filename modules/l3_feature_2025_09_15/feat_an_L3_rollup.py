import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, message):
    public_key = PublicKey.fromString(public_key_bytes)
    r, s = proof
    h = hashlib.sha256(message).digest()
    try:
        sig = public_key.verify(h, s, r)
        return sig
    except:
        return False

proof = (1234567890, 9876543210)
public_key_bytes = b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
message = b'This is a test message'

verification_result = verify_zk_proof(proof, public_key_bytes, message)
print(verification_result)
