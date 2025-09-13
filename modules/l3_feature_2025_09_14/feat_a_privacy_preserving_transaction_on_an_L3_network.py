from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_blinding_factor, receiver_blinding_factor, amount, sender_pubkey, receiver_pubkey):
        self.sender_blinding_factor = sender_blinding_factor
        self.receiver_blinding_factor = receiver_blinding_factor
        self.amount = amount
        self.sender_pubkey = sender_pubkey
        self.receiver_pubkey = receiver_pubkey
        self.transaction_hash = self._generate_hash()

    def _generate_hash(self):
        data_to_hash = str(self.sender_blinding_factor) + str(self.receiver_blinding_factor) + str(self.amount) + str(self.sender_pubkey) + str(self.receiver_pubkey)
        return sha256(data_to_hash.encode()).hexdigest()

    def sign(self, private_key):
        self.signature = private_key.sign(self.transaction_hash.encode())
    
    def verify(self):
        vk = self.sender_pubkey.verifying_key
        return vk.verify(self.signature, self.transaction_hash.encode())


sk = SigningKey.generate(curve=SECP256k1)
pk = sk.get_verifying_key()

tx = ConfidentialTransaction(123, 456, 789, pk, pk)
tx.sign(sk)
is_valid = tx.verify()

