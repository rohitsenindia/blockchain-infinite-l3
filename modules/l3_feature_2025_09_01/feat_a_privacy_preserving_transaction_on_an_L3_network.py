from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class ConfidentialTransaction:
    def __init__(self, sender_pubkey, receiver_pubkey, amount_commitment, asset_id, nonce, signature):
        self.sender_pubkey = sender_pubkey
        self.receiver_pubkey = receiver_pubkey
        self.amount_commitment = amount_commitment
        self.asset_id = asset_id
        self.nonce = nonce
        self.signature = signature

    def to_dict(self):
        return {
            'sender_pubkey': self.sender_pubkey.to_string().hex(),
            'receiver_pubkey': self.receiver_pubkey.to_string().hex(),
            'amount_commitment': self.amount_commitment.hex(),
            'asset_id': self.asset_id,
            'nonce': self.nonce.hex(),
            'signature': self.signature.hex()
        }
    
    @classmethod
    def create(cls, sender_privkey, receiver_pubkey, amount, asset_id, nonce):
        amount_commitment = sha256(amount.to_bytes(32, 'big') + nonce).digest()
        message = amount_commitment + asset_id.encode() + receiver_pubkey.to_string() + nonce
        signature = sender_privkey.sign(message)
        return cls(sender_privkey.get_verifying_key(), receiver_pubkey, amount_commitment, asset_id, nonce, signature)


    def verify(self):
        message = self.amount_commitment + self.asset_id.encode() + self.receiver_pubkey.to_string() + self.nonce
        try:
            return self.sender_pubkey.verify(self.signature, message)
        except:
            return False

    
