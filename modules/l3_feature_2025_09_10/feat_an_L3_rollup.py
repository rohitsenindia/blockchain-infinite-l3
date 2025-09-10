import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, message_hash):
    try:
        public_key = PublicKey.fromString(public_key_bytes)
        r, s = proof
        signature = (r, s)
        
        vk = public_key.toBytes()
        m = hashlib.sha256(message_hash).digest()
        
        sig_r = signature[0]
        sig_s = signature[1]
        
        if not 0 < sig_r <  pow(2,256) and 0 < sig_s < pow(2,256):
            return False

        ver = public_key.verify(m, signature)
        return ver

    except Exception as e:
        return False


proof = (12345678901234567890123456789012, 98765432109876543210987654321098)
private_key = PrivateKey()
public_key = private_key.publicKey()
message = b"test message"
message_hash = hashlib.sha256(message).digest()
signature = private_key.sign(message_hash)
public_key_bytes = public_key.toBytes()

is_valid = verify_zk_proof(signature, public_key_bytes, message_hash)
print(is_valid)


is_valid = verify_zk_proof(proof, public_key_bytes, message_hash)
print(is_valid)
