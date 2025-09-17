import hashlib
import json

class DID:
    def __init__(self, l3_client, public_key):
        self.l3_client = l3_client
        self.public_key = public_key
        self.did = self._generate_did()

    def _generate_did(self):
        key_hash = hashlib.sha256(self.public_key.encode()).hexdigest()
        return f"did:l3:{key_hash}"

    def register(self):
        registration_data = {
            "did": self.did,
            "publicKey": self.public_key
        }
        tx_id = self.l3_client.send_transaction(json.dumps(registration_data))
        return tx_id

    def verify(self, credential):
        signature = credential['signature']
        verified = self.l3_client.verify_signature(credential['payload'], signature, self.public_key)
        return verified

    def get_public_key(self):
      return self.public_key

    def get_did(self):
      return self.did

class L3Client: # Mock L3 Client
    def send_transaction(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def verify_signature(self, payload, signature, public_key):
        # Replace with actual verification logic
        return True

# Example Usage
l3 = L3Client()
my_did = DID(l3, "my_public_key")
tx_id = my_did.register()
print(f"DID registered with transaction ID: {tx_id}")
print(f"My DID: {my_did.get_did()}")
print(f"My Public Key: {my_did.get_public_key()}")

