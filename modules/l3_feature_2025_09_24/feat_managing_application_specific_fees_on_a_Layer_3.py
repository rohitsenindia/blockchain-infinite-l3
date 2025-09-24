from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('YOUR_LAYER_3_PROVIDER_URL'))

abi = [
    {'inputs': [], 'name': 'getFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'},
    {'inputs': [{'internalType': 'uint256', 'name': '_fee', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}
]

contract_address = 'YOUR_CONTRACT_ADDRESS'
contract = w3.eth.contract(address=contract_address, abi=abi)

def get_fee():
    return contract.functions.getFee().call()

def set_fee(new_fee, private_key):
    account = Account.privateKeyToAccount(private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    txn = contract.functions.setFee(new_fee).buildTransaction({
        'chainId': w3.eth.chain_id,
        'gas': 1000000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return w3.toHex(txn_hash)

current_fee = get_fee()
print(f"Current fee: {current_fee}")

new_fee = 100
transaction_hash = set_fee(new_fee, 'YOUR_PRIVATE_KEY')
print(f"Transaction hash: {transaction_hash}")

