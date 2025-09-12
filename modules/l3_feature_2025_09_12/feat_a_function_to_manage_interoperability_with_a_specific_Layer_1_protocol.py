import requests

def interact_with_solana(rpc_url, action, params):
    headers = {'Content-Type': 'application/json'}
    payload = {'jsonrpc': '2.0', 'id': 1, 'method': action, 'params': params}
    response = requests.post(rpc_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['result']

def get_solana_account_balance(rpc_url, address):
    return interact_with_solana(rpc_url, 'getBalance', [address, {"commitment": "finalized"}])

def send_solana_transaction(rpc_url, transaction):
    return interact_with_solana(rpc_url, 'sendTransaction', [transaction])


def get_solana_block_height(rpc_url):
    return interact_with_solana(rpc_url, 'getBlockHeight', [])


def get_solana_block(rpc_url, slot):
    return interact_with_solana(rpc_url, 'getBlock', [slot])
