from typing import Dict, Any

def validate_cross_chain_message(message: Dict[str, Any], oracle_responses: Dict[str, Any], threshold: int) -> bool:
    valid_responses = 0
    for oracle, response in oracle_responses.items():
        if response['signature'] and verify_signature(response['signature'], message['hash'], oracle):
            if response['data'] == message['data']:
                valid_responses += 1
    return valid_responses >= threshold

def verify_signature(signature: str, message_hash: str, oracle_pubkey: str) -> bool:
    # Replace with your actual signature verification logic
    # This is a placeholder, using a dummy verification
    return signature == f"valid_sig_{message_hash}_{oracle_pubkey}"
