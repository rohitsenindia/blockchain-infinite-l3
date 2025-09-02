import hashlib
from hashlib import sha256

def verify_zk_proof(commitment, proof, public_key, challenge):
    inner_hash = sha256(commitment + proof).hexdigest()
    outer_hash = sha256(inner_hash + public_key + challenge).hexdigest()
    return outer_hash == "a_predefined_target_hash"


commitment = "some_commitment_data".encode('utf-8')
proof = "some_zk_proof_data".encode('utf-8')
public_key = "some_public_key_data".encode('utf-8')
challenge = "some_challenge_data".encode('utf-8')

verification_result = verify_zk_proof(commitment, proof, public_key, challenge)

print(verification_result)
