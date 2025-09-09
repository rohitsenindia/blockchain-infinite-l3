from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_blinding_factor, receiver_pubkey, amount_commitment, transaction_fee_commitment, nonce):
        self.sender_blinding_factor = sender_blinding_factor
        self.receiver_pubkey = receiver_pubkey
        self.amount_commitment = amount_commitment
        self.transaction_fee_commitment = transaction_fee_commitment
        self.nonce = nonce
        self.signature = None

    def sign(self, sender_privkey):
        message = self.generate_message()
        signature = sender_privkey.sign(message)
        self.signature = signature

    def generate_message(self):
        message = self.receiver_pubkey.to_string() + self.amount_commitment + self.transaction_fee_commitment + self.nonce
        return sha256(message).digest()

    def verify(self):
        message = self.generate_message()
        return self.receiver_pubkey.verify(self.signature, message)

    def to_dict(self):
      return {'sender_blinding_factor': self.sender_blinding_factor, 'receiver_pubkey': self.receiver_pubkey.to_string(), 'amount_commitment': self.amount_commitment, 'transaction_fee_commitment': self.transaction_fee_commitment, 'nonce': self.nonce, 'signature': self.signature.hex()}


privkey = SigningKey.generate(curve=SECP256k1)
pubkey = privkey.get_verifying_key()
tx = ConfidentialTransaction(b'blinding', pubkey, b'amount_commitment', b'fee_commitment', b'nonce')
tx.sign(privkey)
print(tx.to_dict())
print(tx.verify())
