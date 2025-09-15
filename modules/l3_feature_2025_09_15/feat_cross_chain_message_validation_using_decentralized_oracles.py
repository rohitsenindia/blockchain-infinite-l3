import hashlib
from typing import Dict, Any

def validate_cross_chain_message(message: Dict[str, Any], oracles: Dict[str, str], threshold: int) -> bool:
    signatures = {}
    for oracle_id, oracle_address in oracles.items():
        # Simulate fetching signature from oracle
        signature = hashlib.sha256(str(message).encode()).hexdigest() + oracle_id
        signatures[oracle_id] = signature

    valid_signatures = 0
    for signature in signatures.values():
        if verify_signature(message, signature, oracles):
            valid_signatures += 1

    return valid_signatures >= threshold

def verify_signature(message: Dict[str, Any], signature: str, oracles: Dict[str, str]) -> bool:
    # Placeholder for actual signature verification logic. Replace with your blockchain's specific method.
    # This example uses a simplified check based on message hash and oracle ID.
    message_hash = hashlib.sha256(str(message).encode()).hexdigest()
    return signature.startswith(message_hash)

#Example Usage
message = {"chain_id": 1, "data": "hello"}
oracles = {"oracle1": "address1", "oracle2": "address2", "oracle3": "address3"}
threshold = 2

is_valid = validate_cross_chain_message(message, oracles, threshold)
print(is_valid)
