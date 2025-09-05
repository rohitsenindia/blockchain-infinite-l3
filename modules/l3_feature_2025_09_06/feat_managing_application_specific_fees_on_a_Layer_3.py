from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545')) # Replace with your L3 provider

contract_abi = [
    {'inputs': [], 'name': 'getFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'},
    {'inputs': [{'internalType': 'uint256', 'name': '_fee', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}
]

contract_address = '0xYourContractAddress' # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_fee():
    return contract.functions.getFee().call()

def set_fee(new_fee, private_key):
    account = Account.from_key(private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    tx = contract.functions.setFee(new_fee).buildTransaction({
        'chainId': 1337, # Replace with your L3 chain ID
        'gas': 1000000,
        'nonce': nonce,
        'from': account.address
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.eth.waitForTransactionReceipt(tx_hash)

current_fee = get_fee()
print(f"Current fee: {current_fee}")

# Example of setting a new fee (replace with your private key)
# set_fee(1000, 'YOUR_PRIVATE_KEY') 
