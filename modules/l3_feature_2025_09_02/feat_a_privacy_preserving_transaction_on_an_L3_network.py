from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_pubkey, recipient_pubkey, amount_commitment, nonce, signature):
        self.sender_pubkey = sender_pubkey
        self.recipient_pubkey = recipient_pubkey
        self.amount_commitment = amount_commitment
        self.nonce = nonce
        self.signature = signature

    def verify(self):
        message = self.amount_commitment + self.nonce.to_bytes(32, 'big')
        try:
            vk = VerifyingKey.from_pem(self.sender_pubkey)
            return vk.verify(self.signature, message)
        except Exception as e:
            return False

    @staticmethod
    def create(sender_privkey, recipient_pubkey, amount, nonce):
      sk = SigningKey.from_pem(sender_privkey, curve=SECP256k1)
      amount_commitment = sha256((str(amount)).encode()).hexdigest()
      message = amount_commitment + nonce.to_bytes(32, 'big')
      signature = sk.sign(message)
      return ConfidentialTransaction(sk.get_verifying_key().to_pem(), recipient_pubkey, amount_commitment, nonce, signature)

from ecdsa import VerifyingKey
