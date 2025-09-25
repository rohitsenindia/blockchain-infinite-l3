import hashlib

def verify_zk_proof(proof, public_data, params):
    circuit_hash = hashlib.sha256(public_data.encode()).hexdigest()
    proof_hash = hashlib.sha256(proof.encode()).hexdigest()
    valid =  params["commitment_scheme"].verify(proof_hash, circuit_hash, params["public_key"])
    return valid


#Example usage (replace with actual implementation)
params = {"commitment_scheme": lambda a, b, c: a == hashlib.sha256((b + c).encode()).hexdigest(), "public_key": "some_key"}
proof = "some_proof"
public_data = "some_public_data"

is_valid = verify_zk_proof(proof, public_data, params)
print(is_valid)
