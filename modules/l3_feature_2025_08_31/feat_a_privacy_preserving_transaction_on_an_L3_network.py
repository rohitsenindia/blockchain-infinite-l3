from hashlib import sha256
from secrets import token_bytes

class ConfidentialTransaction:
    def __init__(self, sender_blinding_factor, receiver_blinding_factor, amount, sender_pubkey, receiver_pubkey):
        self.sender_blinding_factor = sender_blinding_factor
        self.receiver_blinding_factor = receiver_blinding_factor
        self.amount = amount
        self.sender_pubkey = sender_pubkey
        self.receiver_pubkey = receiver_pubkey
        self.transaction_hash = self._generate_hash()

    def _generate_hash(self):
        data = self.sender_blinding_factor + self.receiver_blinding_factor + self.amount.to_bytes(32, 'big') + self.sender_pubkey + self.receiver_pubkey
        return sha256(data).hexdigest()

    def __eq__(self, other):
        return self.transaction_hash == other.transaction_hash

    @classmethod
    def generate_random_blinding_factor(cls):
        return token_bytes(32)


    

