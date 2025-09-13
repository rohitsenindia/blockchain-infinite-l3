import hashlib
import json

class DIDL3:
    def __init__(self, l3_client):
        self.l3_client = l3_client

    def create_did(self, public_key):
        did = self._generate_did(public_key)
        self.l3_client.write_transaction({"did": did, "publicKey": public_key})
        return did

    def resolve_did(self, did):
        tx = self.l3_client.read_transaction({"did": did})
        if tx:
            return tx['publicKey']
        return None

    def _generate_did(self, public_key):
        data = json.dumps({"publicKey": public_key}, sort_keys=True)
        digest = hashlib.sha256(data.encode()).hexdigest()
        return f"did:l3:{digest}"


class MockL3Client:
    def __init__(self):
        self.ledger = {}

    def write_transaction(self, data):
        self.ledger[data['did']] = data

    def read_transaction(self, query):
        for did, data in self.ledger.items():
            if data.get('did') == query.get('did'):
                return data
        return None

# Example usage
l3_client = MockL3Client()
did_manager = DIDL3(l3_client)
public_key = "some_public_key"
did = did_manager.create_did(public_key)
resolved_key = did_manager.resolve_did(did)

print(f"DID: {did}")
print(f"Resolved Public Key: {resolved_key}")

