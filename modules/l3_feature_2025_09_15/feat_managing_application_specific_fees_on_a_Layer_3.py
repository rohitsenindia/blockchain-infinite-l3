from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545")) # Replace with your L3 provider

contract_abi = [
    {"inputs": [], "name": "getFee", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "_fee", "type": "uint256"}], "name": "setFee", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "payable": True, "name": "payFee", "outputs": [], "stateMutability": "payable", "type": "function"}
]

contract_address = "0xYourContractAddress" # Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_address)

def get_fee():
    return contract.functions.getFee().call()

def set_fee(new_fee):
    txn = contract.functions.setFee(new_fee).buildTransaction({
        'chainId': 1337, # Replace with your chain ID
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount("0xYourAccountAddress") # Replace with your account address
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key="YourPrivateKey") # Replace with your private key
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return tx_hash.hex()

def pay_fee(amount):
    txn = contract.functions.payFee().buildTransaction({
        'chainId': 1337, # Replace with your chain ID
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'value': amount,
        'nonce': w3.eth.getTransactionCount("0xYourAccountAddress") # Replace with your account address
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key="YourPrivateKey") #Replace with your private key
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return tx_hash.hex()
