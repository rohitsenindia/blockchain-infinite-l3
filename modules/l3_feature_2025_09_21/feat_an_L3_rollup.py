from hashlib import sha256
from ellipticcurve.privateKey import PrivateKey

def verify_zk_proof(proof, public_key, commitment, challenge):
    try:
        priv_key = PrivateKey()
        priv_key.publicKey().toString()
        r = int.from_bytes(proof[:32], 'big')
        s = int.from_bytes(proof[32:64], 'big')
        v = int.from_bytes(proof[64:65], 'big')
        
        assert v == 27 or v == 28
        
        sig = (r,s,v)
        
        message = sha256(commitment.encode()).digest()
        
        verified = priv_key.verify(sig,message)

        return verified

    except Exception as e:
        return False

# Example usage (replace with actual data):
proof = bytes.fromhex("...") # Replace with your proof data
public_key = "04..." # Replace with the public key
commitment = "some commitment"
challenge = "some challenge"

result = verify_zk_proof(proof, public_key, commitment, challenge)
print(f"ZK-proof verification: {result}")
