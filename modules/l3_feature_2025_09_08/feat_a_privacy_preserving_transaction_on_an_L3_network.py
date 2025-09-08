from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_blinding_factor, recipient_blinding_factor, amount, sender_pubkey, recipient_pubkey):
        self.sender_blinding_factor = sender_blinding_factor
        self.recipient_blinding_factor = recipient_blinding_factor
        self.amount = amount
        self.sender_pubkey = sender_pubkey
        self.recipient_pubkey = recipient_pubkey
        self.transaction_hash = self._generate_transaction_hash()

    def _generate_transaction_hash(self):
        data_to_hash = str(self.sender_blinding_factor) + str(self.recipient_blinding_factor) + str(self.amount) + str(self.sender_pubkey) + str(self.recipient_pubkey)
        return sha256(data_to_hash.encode()).hexdigest()

    def sign(self, private_key):
        signature = private_key.sign(self.transaction_hash.encode())
        self.signature = signature
        return signature

    def verify(self):
        vk = self.sender_pubkey.verifying_key
        try:
            return vk.verify(self.signature, self.transaction_hash.encode())
        except:
            return False

#Example Usage
sk = SigningKey.generate(curve=SECP256k1)
pk = sk.get_verifying_key()
another_sk = SigningKey.generate(curve=SECP256k1)
another_pk = another_sk.get_verifying_key()

tx = ConfidentialTransaction(123, 456, 789, pk, another_pk)
tx.sign(sk)
print(tx.verify())
