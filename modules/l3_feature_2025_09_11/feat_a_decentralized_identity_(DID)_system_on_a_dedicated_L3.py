import hashlib
from base64 import b64encode

class DIDL3:
    def __init__(self, l3_client, did_method='l3'):
        self.l3_client = l3_client
        self.did_method = did_method

    def create_did(self, public_key):
        did = f'{self.did_method}:{hashlib.sha256(public_key.encode()).hexdigest()}'
        self.l3_client.write_data(did, {'publicKey': b64encode(public_key.encode()).decode()})
        return did

    def resolve_did(self, did):
        data = self.l3_client.read_data(did)
        if data:
            return {'did': did, 'publicKey': data['publicKey']}
        return None

    def update_did(self, did, new_public_key):
        self.l3_client.update_data(did, {'publicKey': b64encode(new_public_key.encode()).decode()})

    def verify_signature(self, did, data, signature):
        resolved = self.resolve_did(did)
        if resolved:
            public_key = b64decode(resolved['publicKey'].encode())
            # Placeholder for actual verification logic using public_key and signature
            return True # Replace with actual verification
        return False

    def revoke_did(self, did):
        self.l3_client.delete_data(did)

from base64 import b64decode
