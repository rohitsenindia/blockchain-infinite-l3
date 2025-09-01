import hashlib
from ellipticcurve.privateKey import PrivateKey

def verify_zk_proof(proof, public_key_bytes, commitment, message):
    pk = PrivateKey()
    pk.fromString(public_key_bytes)
    r_bytes = proof['r']
    s_bytes = proof['s']
    r = int.from_bytes(r_bytes, byteorder='big')
    s = int.from_bytes(s_bytes, byteorder='big')
    c = int.from_bytes(commitment, byteorder='big')
    m = hashlib.sha256(message).digest()
    m_int = int.from_bytes(m, byteorder='big')
    v = pk.publicKey.verify(r, s, c, m_int)
    return v

proof = {'r': b'\x01' * 32, 's': b'\x02' * 32}
public_key_bytes = b'\x03' * 32
commitment = b'\x04' * 32
message = b'test message'

verified = verify_zk_proof(proof, public_key_bytes, commitment, message)
print(verified)

