from typing import Dict, Any

def validate_cross_chain_message(message: Dict[str, Any], oracle_responses: Dict[str, Any], threshold: int) -> bool:
    valid_responses = 0
    for oracle_id, response in oracle_responses.items():
        if response['signature'] and verify_signature(message['source_chain_id'], message['message_hash'], response['signature'], oracle_id):
            if response['data'] == message['data']:
                valid_responses +=1
    return valid_responses >= threshold

def verify_signature(chain_id: str, message_hash: str, signature: str, oracle_id: str) -> bool:
    # Replace with actual signature verification logic using appropriate crypto library
    # This is a placeholder.  In a real system, this would use a library like pycryptodome
    # and would verify the signature against a known public key for the oracle.
    return True if oracle_id == "trusted_oracle" else False # Placeholder
