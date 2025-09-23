import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec

class DIDL3:
    def __init__(self, key_pair=None):
        if key_pair is None:
            private_key = ec.generate_private_key(ec.SECP256R1())
            self.private_key = private_key
            self.public_key = private_key.public_key()
        else:
            self.private_key = key_pair.private_key
            self.public_key = key_pair.public_key

        self.did = self._generate_did()

    def _generate_did(self):
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        hasher = hashlib.sha256()
        hasher.update(public_bytes)
        return "did:l3:" + hasher.hexdigest()

    def sign(self, message):
        signature = self.private_key.sign(
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        return signature

    def verify(self, message, signature):
        try:
            self.public_key.verify(
                signature,
                message.encode('utf-8'),
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except Exception:
            return False

    def get_did(self):
        return self.did

    def get_public_key(self):
        return self.public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    def to_dict(self):
        return {'did': self.did, 'publicKey': self.get_public_key()}
