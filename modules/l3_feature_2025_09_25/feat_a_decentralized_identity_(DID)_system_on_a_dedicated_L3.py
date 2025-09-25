import hashlib
import json

class DID:
    def __init__(self, l3_client, did_key):
        self.l3_client = l3_client
        self.did_key = did_key
        self.did = self._generate_did()

    def _generate_did(self):
        return "did:l3:" + hashlib.sha256(self.did_key.encode()).hexdigest()

    def get_did(self):
        return self.did

    def issue_credential(self, subject_did, credential):
        credential['issuer'] = self.did
        credential['subject'] = subject_did
        tx_hash = self.l3_client.submit_transaction(json.dumps(credential))
        return tx_hash

    def verify_credential(self, credential_hash):
        credential = self.l3_client.get_transaction(credential_hash)
        return credential and credential['issuer'] and self.l3_client.verify_signature(credential, credential['issuer'])

    def resolve(self, did):
        return self.l3_client.query_did(did)

    def register_did(self):
      self.l3_client.register_did(self.did, self.did_key)

class L3Client: #Mock L3 client
    def __init__(self):
        self.blockchain = {}

    def submit_transaction(self, data):
        tx_hash = hashlib.sha256(data.encode()).hexdigest()
        self.blockchain[tx_hash] = data
        return tx_hash
    def get_transaction(self, tx_hash):
        return self.blockchain.get(tx_hash)
    def verify_signature(self, credential, issuer):
        return True # Replace with actual signature verification
    def query_did(self, did):
        return {"did": did, "key": "some_key"} # Replace with real lookup
    def register_did(self, did, key):
        self.blockchain[did] = key


