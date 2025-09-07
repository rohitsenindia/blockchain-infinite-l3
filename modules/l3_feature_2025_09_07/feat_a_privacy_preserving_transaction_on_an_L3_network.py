from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_blinding_key, receiver_blinding_key, amount, asset_id, nonce):
        self.sender_blinding_key = sender_blinding_key
        self.receiver_blinding_key = receiver_blinding_key
        self.amount = amount
        self.asset_id = asset_id
        self.nonce = nonce
        self.transaction_hash = self._generate_transaction_hash()
    
    def _generate_transaction_hash(self):
        data_string = str(self.amount) + str(self.asset_id) + str(self.nonce)
        return sha256(data_string.encode()).hexdigest()

    def sign(self, sender_private_key):
        sk = SigningKey.from_secret_exponent(sender_private_key, curve=SECP256k1)
        signature = sk.sign(self.transaction_hash.encode())
        return signature

    def verify(self, signature, sender_public_key):
        vk = sk.get_verifying_key()
        try:
            vk.verify(signature, self.transaction_hash.encode())
            return True
        except:
            return False

    def __repr__(self):
        return f"ConfidentialTransaction(amount={self.amount}, asset_id={self.asset_id}, hash={self.transaction_hash})"

