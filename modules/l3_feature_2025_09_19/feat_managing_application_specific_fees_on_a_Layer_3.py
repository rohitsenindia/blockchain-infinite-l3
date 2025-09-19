from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Replace with your L3 provider

abi = [
    {'inputs': [{'internalType': 'uint256', 'name': '_fee', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'},
    {'inputs': [], 'name': 'getFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}
]

contract_address = '0x...' # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=abi)

def set_fee(fee_amount, private_key):
    account = Account.privateKeyToAccount(private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    txn = contract.functions.setFee(fee_amount).buildTransaction({
        'chainId': 1337, #Replace with your chain ID
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': nonce
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

def get_fee():
    return contract.functions.getFee().call()


private_key = '...' # Replace with your private key
set_fee(100, private_key)
print(f"Fee set successfully: {get_fee()}")

