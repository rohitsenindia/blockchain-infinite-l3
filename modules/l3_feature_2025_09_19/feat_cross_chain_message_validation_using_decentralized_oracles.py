import requests

def validate_crosschain_message(message_hash, source_chain_id, target_chain_id, oracle_nodes):
    valid_signatures = 0
    threshold = len(oracle_nodes) // 2 + 1
    for node in oracle_nodes:
        url = f"{node}/validate?hash={message_hash}&source={source_chain_id}&target={target_chain_id}"
        response = requests.get(url)
        if response.status_code == 200 and response.json()['valid']:
            valid_signatures += 1
    return valid_signatures >= threshold
