import hashlib
from typing import Dict, List

def validate_cross_chain_message(message: Dict, oracle_responses: List[Dict]) -> bool:
    message_hash = hashlib.sha256(str(message).encode()).hexdigest()
    valid_responses = 0
    threshold = len(oracle_responses) // 2 + 1
    for response in oracle_responses:
        if response['message_hash'] == message_hash and response['valid']:
            valid_responses +=1
    return valid_responses >= threshold

