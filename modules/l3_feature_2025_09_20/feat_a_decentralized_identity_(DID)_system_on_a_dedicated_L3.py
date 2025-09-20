from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class DID:
    def __init__(self, private_key=None):
        self.private_key = private_key or SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.did = self._generate_did()

    def _generate_did(self):
        public_key_bytes = self.public_key.to_string()
        return "did:l3:" + sha256(public_key_bytes).hexdigest()

    def sign(self, message):
        return self.private_key.sign(message.encode())

    def verify(self, message, signature):
        return self.public_key.verify(signature, message.encode())

    def get_did(self):
        return self.did

    def get_public_key(self):
        return self.public_key.to_string().hex()

    def get_private_key(self):
        return self.private_key.to_string().hex()

    @staticmethod
    def resolve(did):
        # Replace with actual L3 resolution mechanism
        # This is a placeholder
        if did.startswith("did:l3:"):
            #Simulate fetching public key from L3
            return {"publicKey": "0xsimulatedPublicKey"}
        return None

