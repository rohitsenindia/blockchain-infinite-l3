from hashlib import sha256
from gmpy2 import powmod, invert

def verify_zk_proof(public_key, commitment, challenge, response, params):
    g, p, q = params
    left = powmod(g, response, p)
    right = (powmod(commitment, challenge, p) * powmod(public_key, response, p)) % p
    return left == right


# Example usage (replace with actual values from your L3 rollup)
g = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
p = 0x8542d69e4c074f6c6d80890f0a6607f6399f60f256b67b77a97290d288571f45
q = 0x7fffffffffffffffffffffff7ccaa5a4d8f8049467c8d0860a18566
public_key = 0x123456789abcdef0123456789abcdef01234567
commitment = sha256(b'secret').hexdigest()
challenge = 0xdeadbeef
response = 0xcafebabe

params = (g,p,q)

is_valid = verify_zk_proof(public_key, int(commitment,16), challenge, response, params)

print(is_valid)

