import hashlib
from py_ecc.bls import G1, G2, pairing

def verify_zk_proof(vk, proof, public_inputs):
    assert len(public_inputs) == 2
    a, b, c = proof
    A = G1.multiply(a, vk[0])
    B = G1.multiply(b, vk[1])
    C = G1.multiply(c, vk[2])
    lhs = pairing(A, G2) * pairing(B, G2) * pairing(C, G2)
    rhs = pairing(G1, G2) * pairing(G1.multiply(public_inputs[0], vk[3]), G2) * pairing(G1.multiply(public_inputs[1], vk[4]), G2)

    return lhs == rhs


vk = (G1.normalize(b'\x01'), G1.normalize(b'\x02'), G1.normalize(b'\x03'), G1.normalize(b'\x04'), G1.normalize(b'\x05'))
proof = (1,2,3)
public_inputs = (10, 20)

is_valid = verify_zk_proof(vk, proof, public_inputs)
print(is_valid)

