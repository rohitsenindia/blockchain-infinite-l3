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
        data = {"did": self.did, "publicKey": self.public_key}
        tx_id = self.l3_client.send_transaction(json.dumps(data))
        return tx_id

    def verify(self, signature, message):
        return self.l3_client.verify_signature(self.public_key, signature, message)


class L3Client:  #Mock L3 client
    def __init__(self):
        self.blockchain = {}

    def send_transaction(self, data):
        tx_id = hashlib.sha256(data.encode()).hexdigest()
        self.blockchain[tx_id] = data
        return tx_id

    def verify_signature(self, public_key, signature, message):
        # Replace with actual signature verification logic
        return True # Placeholder for verification

# Example usage
l3 = L3Client()
did = DID(l3, "some_public_key")
tx_id = did.register()
print(f"DID registered with tx_id: {tx_id}")
print(f"Generated DID: {did.did}")

verification_result = did.verify("some_signature", "some_message")
print(f"Verification result: {verification_result}")

