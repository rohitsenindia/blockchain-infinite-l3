import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec

class DID:
    def __init__(self, private_key=None):
        if private_key is None:
            private_key = ec.generate_private_key(ec.SECP256R1())
        self.private_key = private_key
        self.public_key = self.private_key.public_key()
        self.did = self._generate_did()

    def _generate_did(self):
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        hasher = hashlib.sha256()
        hasher.update(public_bytes)
        did = "did:l3:" + hasher.hexdigest()
        return did

    def sign(self, message):
        return self.private_key.sign(message.encode(), ec.ECDSA(hashes.SHA256()))

    def verify(self, signature, message, public_key):
        try:
            public_key.verify(signature, message.encode(), ec.ECDSA(hashes.SHA256()))
            return True
        except Exception:
            return False

    def get_public_key_pem(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def get_private_key_pem(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
