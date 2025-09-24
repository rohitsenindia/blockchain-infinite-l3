import hashlib
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey

def verify_zk_proof(proof, public_key_bytes, message_hash):
    public_key = PublicKey.fromString(public_key_bytes)
    r, s = proof
    r_point = PublicKey(r, None)
    s_point = PublicKey(s, None)

    hash_bytes = hashlib.sha256(message_hash.encode()).digest()

    v = r_point.x + s_point.x + public_key.x
    v_point = PublicKey(v, None)
    
    if v_point.verify(hash_bytes, s_point):
        return True
    else:
        return False


proof = (1234567890, 9876543210)
public_key_bytes = b'\x04\x88\x7a\x5f\x31\x70\x9b\x7f\x0d\x8a\x80\x7f\x10\x64\x92\x23\x4c\x67\x2d\x57\xb1\x4a\x85\x28\x42\x46\x0e\x96\x53\xf3\x58\x9a\x52\xf4\x02'
message_hash = 'testmessage'

verification_result = verify_zk_proof(proof, public_key_bytes, message_hash)

print(verification_result)
