import hashlib

def verify_zk_proof(proof, public_data, circuit_params):
    h = hashlib.sha256()
    h.update(proof + public_data + circuit_params.encode())
    digest = h.hexdigest()
    return digest == circuit_params.split(':')[1]

proof = "a_valid_zk_proof"
public_data = "transaction_data"
circuit_params = "circuit_id:a_valid_hash"

is_valid = verify_zk_proof(proof, public_data, circuit_params)

print(is_valid)
