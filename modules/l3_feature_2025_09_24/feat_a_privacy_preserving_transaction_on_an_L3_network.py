from hashlib import sha256
from cryptography.fernet import Fernet

class PrivacyPreservingTransaction:
    def __init__(self, sender_zkp, receiver_zkp, amount, nonce, l2_tx_hash):
        self.sender_zkp = sender_zkp
        self.receiver_zkp = receiver_zkp
        self.amount = amount
        self.nonce = nonce
        self.l2_tx_hash = l2_tx_hash
        self.generate_hash()

    def generate_hash(self):
        data_string = f"{self.sender_zkp}{self.receiver_zkp}{self.amount}{self.nonce}{self.l2_tx_hash}"
        self.transaction_hash = sha256(data_string.encode()).hexdigest()

    def encrypt_data(self, key):
        f = Fernet(key)
        encrypted_data = f.encrypt(f"{self.amount}:{self.nonce}".encode())
        return encrypted_data

    def decrypt_data(self, key):
        f = Fernet(key)
        decrypted_data = f.decrypt(self.encrypted_data).decode()
        amount, nonce = decrypted_data.split(':')
        return int(amount), int(nonce)


    def __str__(self):
        return f"Transaction Hash: {self.transaction_hash}\nSender ZKP: {self.sender_zkp}\nReceiver ZKP: {self.receiver_zkp}\nEncrypted Data: {self.encrypted_data}"


# Example usage (replace with actual ZKPs and keys)
sender_zkp = "zkp_sender"
receiver_zkp = "zkp_receiver"
key = Fernet.generate_key()
tx = PrivacyPreservingTransaction(sender_zkp, receiver_zkp, 10, 1234, "l2_hash")
tx.encrypted_data = tx.encrypt_data(key)
print(tx)
amount, nonce = tx.decrypt_data(key)
print(f"Decrypted Amount: {amount}, Decrypted Nonce: {nonce}")

