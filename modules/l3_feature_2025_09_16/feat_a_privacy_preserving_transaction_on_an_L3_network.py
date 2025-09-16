from dataclasses import dataclass, field
from typing import List, Any

@dataclass(frozen=True)
class ConfidentialTransaction:
    sender_commitment: bytes
    recipient_commitment: bytes
    amount_commitment: bytes
    nonce: bytes
    sender_blinding_factor: bytes
    recipient_blinding_factor: bytes
    range_proof: bytes
    transaction_id: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'transaction_id', self._generate_transaction_id())

    def _generate_transaction_id(self) -> str:
        import hashlib
        data_to_hash = self.sender_commitment + self.recipient_commitment + self.amount_commitment + self.nonce
        return hashlib.sha256(data_to_hash).hexdigest()


@dataclass
class L3Transaction:
    transaction: ConfidentialTransaction
    metadata: dict = field(default_factory=dict)
    signatures: List[bytes] = field(default_factory=list)

    def add_signature(self, signature: bytes):
        self.signatures.append(signature)

    def verify_signatures(self) -> bool:
        # Placeholder for signature verification logic.  Replace with actual implementation.
        return all(len(sig) > 0 for sig in self.signatures)

    

transaction = L3Transaction(
    transaction=ConfidentialTransaction(
        sender_commitment=b'sender_commitment',
        recipient_commitment=b'recipient_commitment',
        amount_commitment=b'amount_commitment',
        nonce=b'nonce',
        sender_blinding_factor=b'sender_bf',
        recipient_blinding_factor=b'recipient_bf',
        range_proof=b'range_proof'
    ),
    metadata={"fee": 10, "timestamp": 1678886400}
)

transaction.add_signature(b'signature1')
transaction.add_signature(b'signature2')

print(transaction.verify_signatures())
print(transaction.transaction.transaction_id)
