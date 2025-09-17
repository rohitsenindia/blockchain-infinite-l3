from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class DIDL3:
    def __init__(self, seed):
        sk = SigningKey.generate(curve=SECP256k1, seed=seed.encode())
        self.vk = sk.get_verifying_key()
        self.did = "did:l3:" + sha256(self.vk.to_string()).hexdigest()

    def sign(self, message):
        sk = SigningKey.generate(curve=SECP256k1, seed=message.encode())
        signature = sk.sign(message.encode())
        return signature

    def verify(self, message, signature):
        try:
            return self.vk.verify(signature, message.encode())
        except:
            return False

    def get_did(self):
        return self.did

    def get_vk(self):
        return self.vk.to_string()
