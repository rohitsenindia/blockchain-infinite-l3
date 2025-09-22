import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, message_hash):
    public_key = PublicKey.fromString(public_key_bytes)
    r, s = proof
    signature = (r,s)
    r_bytes = r.to_bytes(32, byteorder='big')
    s_bytes = s.to_bytes(32, byteorder='big')
    
    signature_hash = hashlib.sha256(r_bytes + s_bytes).digest()
    
    try:
        public_key.verify(signature_hash, message_hash)
        return True
    except Exception:
        return False

proof = (12345678901234567890123456789012, 9876543210987654321098765432109)
public_key_bytes = bytes.fromhex("0471143b09a68f9b71c782573d84c21e06b02f213c3844c6196d80e910f86d85e502844d18b975a75d8e26d0146ab72623b6227e115324f94884d2f1177e2676")
message_hash = hashlib.sha256(b"test message").digest()

verification_result = verify_zk_proof(proof, public_key_bytes, message_hash)
print(verification_result)

