from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('YOUR_LAYER_3_PROVIDER_URL'))

abi = [
    {'inputs': [{'internalType': 'uint256', 'name': 'feeAmount', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'},
    {'inputs': [], 'name': 'getFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'},
    {'inputs': [], 'name': 'withdrawFees', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}
]

contract_address = 'YOUR_CONTRACT_ADDRESS'
contract = w3.eth.contract(address=contract_address, abi=abi)

private_key = 'YOUR_PRIVATE_KEY'
account = Account.privateKeyToAccount(private_key)

def set_fee(amount):
    txn = contract.functions.setFee(amount).buildTransaction({
        'chainId': w3.eth.chain_id,
        'nonce': w3.eth.getTransactionCount(account.address),
        'gas': 1000000,
        'gasPrice': w3.eth.gas_price
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)

def get_fee():
    return contract.functions.getFee().call()

def withdraw_fees():
    txn = contract.functions.withdrawFees().buildTransaction({
        'chainId': w3.eth.chain_id,
        'nonce': w3.eth.getTransactionCount(account.address),
        'gas': 1000000,
        'gasPrice': w3.eth.gas_price
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.toHex(tx_hash)
