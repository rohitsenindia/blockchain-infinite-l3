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
        digest = hashlib.sha256(public_bytes).hexdigest()
        return f"did:l3:{digest}"

    def sign(self, message):
        signature = self.private_key.sign(
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return signature

    def verify(self, message, signature):
        try:
            self.public_key.verify(
                signature,
                message.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

    def get_did(self):
        return self.did

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
