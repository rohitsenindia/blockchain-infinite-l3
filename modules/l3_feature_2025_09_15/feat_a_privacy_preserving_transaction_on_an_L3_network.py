from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ConfidentialTransaction:
    sender_commitment: bytes
    receiver_commitment: bytes
    amount_commitment: bytes
    range_proof: bytes
    nonce: bytes
    zk_proof: bytes
    transaction_id: str = None

@dataclass
class L3Transaction:
    inner_transaction: ConfidentialTransaction
    l3_metadata: dict

    def __post_init__(self):
        self.transaction_id = self.generate_transaction_id()

    def generate_transaction_id(self)->str:
        import hashlib
        data_to_hash = (str(self.inner_transaction)+str(self.l3_metadata)).encode('utf-8')
        return hashlib.sha256(data_to_hash).hexdigest()


