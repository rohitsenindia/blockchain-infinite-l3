import hashlib
import secrets

def verify_zk_proof(proof, public_key, commitment, challenge):
    gamma = int.from_bytes(proof[:32], 'big')
    z = int.from_bytes(proof[32:64], 'big')
    c = hashlib.sha256((public_key + commitment + challenge).encode()).hexdigest()
    left = (gamma * pow(2, 256, 10**10) + int(c, 16)) % (10**10)
    right = pow(z,2,10**10)
    return left == right


proof = secrets.token_bytes(64)
public_key = "some_public_key"
commitment = "some_commitment"
challenge = "some_challenge"

verification_result = verify_zk_proof(proof, public_key, commitment, challenge)

print(verification_result)
