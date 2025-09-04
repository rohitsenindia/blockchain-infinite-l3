from hashlib import sha256
from base64 import b64encode, b64decode

class DIDL3:
    def __init__(self, l3_client):
        self.l3 = l3_client

    def create_did(self, public_key):
        did = f"did:l3:{b64encode(sha256(public_key.encode()).digest()).decode()}"
        self.l3.register_did(did, public_key)
        return did

    def resolve_did(self, did):
        return self.l3.get_did_data(did)

    def verify_signature(self, did, data, signature):
        public_key = self.resolve_did(did)['publicKey']
        try:
            return public_key.verify(data, signature)
        except Exception:
            return False

    def update_did(self, did, new_public_key):
      self.l3.update_did(did, new_public_key)


    def revoke_did(self, did):
        self.l3.revoke_did(did)


class MockL3Client:
    def __init__(self):
        self.dids = {}

    def register_did(self, did, public_key):
        self.dids[did] = {'publicKey': public_key}

    def get_did_data(self, did):
        return self.dids.get(did)

    def update_did(self, did, new_public_key):
        self.dids[did]['publicKey'] = new_public_key

    def revoke_did(self, did):
        del self.dids[did]



# Example usage with a mock L3 client
l3_client = MockL3Client()
did_manager = DIDL3(l3_client)
test_key = "test_public_key"
did = did_manager.create_did(test_key)
resolved_data = did_manager.resolve_did(did)
print(f"Resolved DID data: {resolved_data}")

