import hashlib
from typing import Dict, List

def validate_crosschain_message(message: Dict, oracles: List[str], threshold: int) -> bool:
    message_hash = hashlib.sha256(str(message).encode()).hexdigest()
    valid_signatures = 0
    for oracle in oracles:
        # Replace with actual signature verification logic
        signature = get_oracle_signature(oracle, message_hash) 
        if verify_signature(signature, message_hash, oracle):
            valid_signatures += 1
    return valid_signatures >= threshold

def get_oracle_signature(oracle: str, message_hash: str) -> str:
    #Simulate fetching signature from oracle; Replace with actual oracle interaction
    signatures = {"oracle1":"sig1", "oracle2":"sig2", "oracle3":"sig3"}
    return signatures.get(oracle,"")

def verify_signature(signature: str, message_hash: str, oracle: str) -> bool:
    # Replace with actual signature verification using oracle's public key
    return signature != "" and oracle in ["oracle1", "oracle2", "oracle3"]
