import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def validate_cross_chain_message(message, source_chain_id, oracle_signatures, oracle_public_keys):
    message_hash = hashlib.sha256(message.encode()).digest()
    combined_signature = b''
    for sig in oracle_signatures:
        combined_signature += sig
    combined_hash = hashlib.sha256(combined_signature).digest()
    verifier = ec.ECDSA(hashes.SHA256())
    for i, pub_key in enumerate(oracle_public_keys):
        try:
            verifier.verify(oracle_signatures[i], combined_hash, pub_key)
        except:
            return False
    return True

#Example Usage (replace with actual data):
message = "This is a cross-chain message"
source_chain_id = "ChainA"
oracle_signatures = [b'signature1',b'signature2',b'signature3']
oracle_public_keys = [ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(),b'pubkey1'), ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(),b'pubkey2'), ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(),b'pubkey3')]

is_valid = validate_cross_chain_message(message, source_chain_id, oracle_signatures, oracle_public_keys)
print(is_valid)

