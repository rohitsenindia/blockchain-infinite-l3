import requests

def interact_with_solana(rpc_url, action, params={}):
    headers = {'Content-Type': 'application/json'}
    payload = {'jsonrpc': '2.0', 'id': 1, 'method': action, 'params': params}
    response = requests.post(rpc_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['result']

def get_solana_balance(rpc_url, address):
    return interact_with_solana(rpc_url, 'getBalance', {'commitment': 'finalized', 'account': address})

def send_solana_transaction(rpc_url, transaction):
    return interact_with_solana(rpc_url, 'sendTransaction', {'transaction': transaction})

def get_solana_block_height(rpc_url):
    return interact_with_solana(rpc_url, 'getBlockHeight')


