import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec

class DIDManager:
    def __init__(self, l3_client):
        self.l3_client = l3_client

    def create_did(self, key_pair):
        public_key = key_pair.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        did = hashlib.sha256(public_key).hexdigest()
        self.l3_client.register_did(did, public_key)
        return did

    def verify_signature(self, did, message, signature):
        public_key = self.l3_client.get_public_key(did)
        if public_key is None:
            return False
        public_key = serialization.load_pem_public_key(public_key)
        try:
            public_key.verify(
                signature,
                message,
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

    def resolve_did(self, did):
        return self.l3_client.get_did_info(did)


class MockL3Client:
    def __init__(self):
        self.dids = {}

    def register_did(self, did, public_key):
        self.dids[did] = {'public_key': public_key}

    def get_public_key(self, did):
        return self.dids.get(did, {}).get('public_key')

    def get_did_info(self, did):
        return self.dids.get(did)


#Example usage
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
l3_client = MockL3Client()
did_manager = DIDManager(l3_client)
did = did_manager.create_did(private_key)
print(f"DID: {did}")

#Verification example (replace with actual message and signature)
message = b'test message'
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
verification_result = did_manager.verify_signature(did, message, signature)
print(f"Verification Result: {verification_result}")

