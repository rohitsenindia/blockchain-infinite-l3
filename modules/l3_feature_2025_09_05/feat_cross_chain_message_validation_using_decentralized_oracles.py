import hashlib
from typing import Dict, List

def validate_cross_chain_message(message: Dict, oracles: List[str], threshold: int) -> bool:
    message_hash = hashlib.sha256(str(message).encode()).hexdigest()
    oracle_responses = {}
    for oracle in oracles:
        # Simulate fetching response from decentralized oracle
        response = simulate_oracle_response(oracle, message_hash)
        oracle_responses[oracle] = response

    valid_responses = sum(1 for response in oracle_responses.values() if response == "valid")
    return valid_responses >= threshold

def simulate_oracle_response(oracle: str, message_hash: str) -> str:
    # Simulate oracle's validation logic, replace with actual oracle interaction
    # This could involve making API calls, checking signatures, etc.
    if oracle == "oracle_1" and message_hash == "test_hash":
      return "valid"
    elif oracle == "oracle_2" and message_hash == "test_hash":
      return "valid"
    elif oracle == "oracle_3" and message_hash == "test_hash":
      return "invalid"
    else:
        return "invalid"


#Example Usage
message = {"sender": "chainA", "receiver": "chainB", "data": "test_data"}
oracles = ["oracle_1", "oracle_2", "oracle_3"]
threshold = 2
is_valid = validate_cross_chain_message(message, oracles, threshold)
print(is_valid) # True if at least 2 oracles confirm the message

