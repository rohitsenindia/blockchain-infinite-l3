from hashlib import sha256
from ecdsa import SigningKey, VerifyingKey

class ConfidentialTransaction:
    def __init__(self, sender_blinding_factor, receiver_blinding_factor, amount, sender_pubkey, receiver_pubkey):
        self.sender_blinding_factor = sender_blinding_factor
        self.receiver_blinding_factor = receiver_blinding_factor
        self.amount = amount
        self.sender_pubkey = sender_pubkey
        self.receiver_pubkey = receiver_pubkey
        self.transaction_hash = self._compute_hash()

    def _compute_hash(self):
        data_to_hash = str(self.sender_blinding_factor) + str(self.receiver_blinding_factor) + str(self.amount) + str(self.sender_pubkey) + str(self.receiver_pubkey)
        return sha256(data_to_hash.encode()).hexdigest()

    def sign(self, private_key):
        signature = private_key.sign(self.transaction_hash.encode())
        return signature

    def verify(self, signature, public_key):
        try:
            return public_key.verify(signature, self.transaction_hash.encode())
        except:
            return False


# Example Usage (replace with your actual key generation)
sk = SigningKey.generate()
vk = sk.get_verifying_key()
sk2 = SigningKey.generate()
vk2 = sk2.get_verifying_key()

tx = ConfidentialTransaction(123, 456, 10, vk, vk2)
signature = tx.sign(sk)
is_valid = tx.verify(signature, vk)

print(is_valid)

