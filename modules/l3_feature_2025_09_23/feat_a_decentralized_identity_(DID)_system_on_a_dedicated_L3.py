import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec

class DIDManager:
    def __init__(self, l3_client):
        self.l3_client = l3_client

    def create_did(self, private_key_pem):
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None
        )
        public_key = private_key.public_key()
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        did = self._generate_did(public_key_bytes)
        self.l3_client.register_did(did, public_key_bytes)
        return did

    def _generate_did(self, public_key_bytes):
        hasher = hashlib.sha256()
        hasher.update(public_key_bytes)
        did = "did:l3:" + hasher.hexdigest()
        return did

    def verify_signature(self, did, message, signature):
        public_key_bytes = self.l3_client.get_public_key(did)
        public_key = serialization.load_pem_public_key(public_key_bytes)
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
        return self.l3_client.get_public_key(did)


class MockL3Client:
    def __init__(self):
        self.dids = {}

    def register_did(self, did, public_key):
        self.dids[did] = public_key

    def get_public_key(self, did):
        return self.dids.get(did)


# Example usage (requires cryptography library)
client = MockL3Client()
manager = DIDManager(client)

private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

did = manager.create_did(private_key_pem)
print(f"Created DID: {did}")

#Further verification and resolution methods would follow here.

