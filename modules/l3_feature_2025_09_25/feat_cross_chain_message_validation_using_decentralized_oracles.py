import requests

def validate_cross_chain_message(message_hash, source_chain_id, oracles):
    valid_signatures = 0
    required_signatures = len(oracles) * 2 // 3

    for oracle_url in oracles:
        try:
            response = requests.get(f"{oracle_url}/validate?hash={message_hash}&source_chain={source_chain_id}")
            response.raise_for_status()
            if response.json()["valid"]:
                valid_signatures += 1
        except requests.exceptions.RequestException:
            pass  

    return valid_signatures >= required_signatures
