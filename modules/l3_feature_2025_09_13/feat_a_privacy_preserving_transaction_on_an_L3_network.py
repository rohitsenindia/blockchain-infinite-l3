from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

class PrivateTransaction:
    def __init__(self, sender_key, recipient_zkp, amount, data):
        self.sender_key = sender_key
        self.recipient_zkp = recipient_zkp
        self.amount = amount
        self.data = data
        self.signature = self.sign()
        self.hash = self.calculate_hash()

    def sign(self):
        sk = SigningKey.from_secret_exponent(int(self.sender_key, 16), curve=SECP256k1)
        message_hash = sha256(f"{self.recipient_zkp}{self.amount}{self.data}".encode()).digest()
        return sk.sign(message_hash).hex()
    
    def calculate_hash(self):
        transaction_data = f"{self.sender_key}{self.recipient_zkp}{self.amount}{self.data}{self.signature}"
        return sha256(transaction_data.encode()).hexdigest()

    def verify(self):
        vk = self.sender_key
        message_hash = sha256(f"{self.recipient_zkp}{self.amount}{self.data}".encode()).digest()
        try:
            vk = self.sender_key
            vk = bytes.fromhex(vk[2:]) #remove 0x prefix if present
            vk = SigningKey.from_string(vk, curve=SECP256k1).get_verifying_key()
            return vk.verify(bytes.fromhex(self.signature), message_hash)
        except:
            return False


#Example usage (replace with actual ZKP and keys)
sender_key = "0x1234567890abcdef1234567890abcdef12345678" # Replace with actual private key
recipient_zkp = "zkp_data_placeholder" # Replace with actual zero-knowledge proof
amount = 10
data = "transaction details"
tx = PrivateTransaction(sender_key, recipient_zkp, amount, data)
print(f"Transaction Hash: {tx.hash}")
print(f"Transaction Verified: {tx.verify()}")

