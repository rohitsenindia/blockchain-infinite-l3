from dataclasses import dataclass, field
from typing import List, Dict

@dataclass(frozen=True)
class ConfidentialTransaction:
    sender_blinding_factor: int
    recipient_blinding_factor: int
    amount_commitment: int
    nonce: int
    sender_zk_proof: bytes
    recipient_zk_proof: bytes
    metadata: Dict = field(default_factory=dict)
    l2_transaction_hash: str = ""


@dataclass(frozen=True)
class L3Block:
    transactions: List[ConfidentialTransaction]
    previous_hash: str = ""
    block_number: int = 0

    

