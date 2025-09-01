from hashlib import sha256
from ellipticcurve.privateKey import PrivateKey

def verify_zk_proof(proof, public_key, commitment):
    r, s = proof
    pubkey_bytes = bytes.fromhex(public_key)
    commitment_bytes = bytes.fromhex(commitment)

    try:
      pk = PrivateKey()
      pk.publicKey().toBytes()
      
      if len(pubkey_bytes) != 65:
          return False

      h = sha256(commitment_bytes + r.to_bytes(32, 'big')).hexdigest()
      signature = pk.sign(h)
      
      if signature[0:32] != s:
        return False

      verified = pk.publicKey().verify(h, signature)
      return verified

    except Exception as e:
        return False

#Example usage (replace with actual values from rollup)
proof = (1234567890, b'\x01'*32) #replace with actual r and s from proof
public_key = '02d9888c21880472e6787a2d1e239c44679e89a1873681f6a3b38f0a062074c13d'  #Replace with the actual public key
commitment = 'c0ffee' # replace with actual commitment
verified = verify_zk_proof(proof, public_key, commitment)
print(verified)

