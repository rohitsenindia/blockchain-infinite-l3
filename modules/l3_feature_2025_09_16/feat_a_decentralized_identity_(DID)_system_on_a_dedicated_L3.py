import hashlib
import json

class DID:
    def __init__(self, l3_client, seed):
        self.l3_client = l3_client
        self.seed = seed
        self.did = self._generate_did()

    def _generate_did(self):
        seed_hash = hashlib.sha256(self.seed.encode()).hexdigest()
        return f"did:l3:{seed_hash}"

    def register(self, metadata):
        tx = {
            "type": "DIDRegister",
            "did": self.did,
            "metadata": metadata
        }
        return self.l3_client.send_transaction(tx)

    def update_metadata(self, metadata):
        tx = {
            "type": "DIDUpdate",
            "did": self.did,
            "metadata": metadata
        }
        return self.l3_client.send_transaction(tx)

    def get_metadata(self):
        return self.l3_client.get_did_metadata(self.did)

    def verify_signature(self, data, signature):
        return self.l3_client.verify_signature(data, signature, self.did)


class L3Client:
    def send_transaction(self, tx):
        #Simulate L3 interaction - replace with actual L3 communication
        return json.dumps({"txHash": hashlib.sha256(json.dumps(tx).encode()).hexdigest()})

    def get_did_metadata(self, did):
        #Simulate L3 interaction - replace with actual L3 communication
        return {"name": "Example User", "email": "example@email.com"}

    def verify_signature(self, data, signature, did):
        #Simulate L3 interaction - replace with actual L3 communication
        return True

# Example usage
l3_client = L3Client()
my_did = DID(l3_client, "mysecretseed")
registration_result = my_did.register({"name": "Alice", "email": "alice@example.com"})
print(registration_result)
metadata = my_did.get_metadata()
print(metadata)

