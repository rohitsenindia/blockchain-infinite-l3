from hashlib import sha256
from base64 import b64encode, b64decode

class PrivateTransaction:
    def __init__(self, sender_zkp, recipient_zkp, amount, data, l3_metadata):
        self.sender_zkp = sender_zkp
        self.recipient_zkp = recipient_zkp
        self.amount = amount
        self.data = data
        self.l3_metadata = l3_metadata
        self.hash = self._generate_hash()

    def _generate_hash(self):
        data_string = f"{self.sender_zkp}{self.recipient_zkp}{self.amount}{self.data}{self.l3_metadata}"
        data_bytes = data_string.encode('utf-8')
        return b64encode(sha256(data_bytes).digest()).decode('utf-8')

    def to_dict(self):
        return {
            'sender_zkp': self.sender_zkp,
            'recipient_zkp': self.recipient_zkp,
            'amount': self.amount,
            'data': self.data,
            'l3_metadata': self.l3_metadata,
            'hash': self.hash
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['sender_zkp'], data['recipient_zkp'], data['amount'], data['data'], data['l3_metadata'])

    
