import hashlib
import secrets

def verify_zk_proof(proof, public_key, commitment):
    r, s = proof
    c = hashlib.sha256(public_key + commitment + str(r)).hexdigest()
    if int(c, 16) % 2**256 == (s - r) % 2**256:
        return True
    return False

# Example Usage
public_key = secrets.token_bytes(32)
commitment = secrets.token_bytes(32)
r = secrets.randbits(256)
s = int(hashlib.sha256(public_key + commitment + str(r)).hexdigest(), 16) + r

proof = (r, s)

is_valid = verify_zk_proof(proof, public_key, commitment)

if is_valid:
    print("Proof Verified")
else:
    print("Proof Invalid")

