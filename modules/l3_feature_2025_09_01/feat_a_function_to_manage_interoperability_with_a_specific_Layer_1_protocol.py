import requests
from eth_account import Account

def interact_with_layer1(private_key, contract_address, function_name, function_args, network='mainnet'):
    account = Account.from_key(private_key)
    url = f'https://{network}.infura.io/v3/YOUR_INFURA_PROJECT_ID' #Replace with your Infura project ID
    nonce = requests.get(f'{url}/eth_getTransactionCount?address={account.address}&tag=latest').json()['result']
    gas_price = requests.get(f'{url}/eth_gasPrice').json()['result']

    transaction = {
        'nonce': int(nonce, 16),
        'gasPrice': int(gas_price, 16),
        'gas': 2000000, # Adjust as needed
        'to': contract_address,
        'value': 0,
        'data': function_signature(function_name, function_args),
        'chainId': 1 if network == 'mainnet' else 3  # Mainnet or Ropsten
    }
    signed_txn = account.signTransaction(transaction)
    response = requests.post(f'{url}/eth_sendRawTransaction', json={'params': [signed_txn.rawTransaction.hex()]})
    return response.json()

def function_signature(function_name, args):
    #Simplified signature generation - replace with a robust ABI encoding library in production
    return '0x' + function_name + ''.join([str(arg) for arg in args])


