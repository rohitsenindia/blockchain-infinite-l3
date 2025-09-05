from hashlib import sha256
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

class PrivateTransaction:
    def __init__(self, sender_private_key, recipient_zk_address, amount, data):
        self.sender_private_key = sender_private_key
        self.recipient_zk_address = recipient_zk_address
        self.amount = amount
        self.data = data
        self.signature = self._sign()
    
    def _sign(self):
        digest = sha256(self._serialize()).digest()
        signature = self.sender_private_key.sign(
            digest,
            ec.ECDSA(hashes.SHA256())
        )
        return signature

    def _serialize(self):
        return (str(self.sender_private_key.public_key().public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
        )) + self.recipient_zk_address + str(self.amount) + self.data).encode()

    def verify(self):
        digest = sha256(self._serialize()).digest()
        public_key = serialization.load_pem_public_key(self.sender_private_key.public_key().public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
        ))
        try:
            public_key.verify(self.signature, digest, ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False


# Example usage (replace with actual keys and addresses)
private_key = ec.generate_private_key(ec.SECP256R1())
transaction = PrivateTransaction(private_key, "zkAddress", 10, "some_data")
is_valid = transaction.verify()

