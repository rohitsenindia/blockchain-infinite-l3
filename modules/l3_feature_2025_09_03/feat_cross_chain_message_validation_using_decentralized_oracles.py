import hashlib
from typing import Dict, Any

def validate_cross_chain_message(message: Dict[str, Any], oracle_responses: Dict[str, Any], threshold: int) -> bool:
    message_hash = hashlib.sha256(str(message).encode()).hexdigest()
    valid_responses = 0
    for oracle_id, response in oracle_responses.items():
        if response['message_hash'] == message_hash and response['valid']:
            valid_responses +=1
    return valid_responses >= threshold

```
