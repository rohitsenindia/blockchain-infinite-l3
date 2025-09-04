import hashlib
from py_ecc.fields import optimized_bls12_381_FQ as FQ
from py_ecc.bls import G1, G2, pairing

def verify_zk_proof(proof, public_key, commitment):
    (A, B, C) = proof
    (x, y) = public_key
    e = hashlib.sha256(commitment + public_key).digest()
    e_int = int.from_bytes(e, 'big')
    e_fq = FQ(e_int)

    lhs = pairing(A - e_fq * G1, G2)
    rhs = pairing(B, G2) * pairing(x * G1, G2) * pairing(C - y * G1, G2)
    return lhs == rhs

proof = ((FQ(1234), FQ(5678), FQ(9012)),)
public_key = (FQ(10), FQ(20))
commitment = b'test_commitment'
result = verify_zk_proof(proof, public_key, commitment)
print(result)

