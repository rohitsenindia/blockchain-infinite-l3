from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545")) # Replace with your L3 provider

abi = [
    {
        "inputs": [],
        "name": "getFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_fee", "type": "uint256"}],
        "name": "setFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

contract_address = "0xYourContractAddress" # Replace with your deployed contract address
contract = w3.eth.contract(address=contract_address, abi=abi)

def get_fee():
    return contract.functions.getFee().call()

def set_fee(new_fee, private_key):
    account = Account.from_key(private_key)
    nonce = w3.eth.getTransactionCount(account.address)
    tx = contract.functions.setFee(new_fee).buildTransaction({
        'chainId': 1337, #Replace with your L3 chain ID
        'nonce': nonce,
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei')
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key=private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return w3.eth.waitForTransactionReceipt(tx_hash)

current_fee = get_fee()
print(f"Current fee: {current_fee}")

#Example of setting a new fee.  Replace with your private key
#set_fee(100, "your_private_key")

