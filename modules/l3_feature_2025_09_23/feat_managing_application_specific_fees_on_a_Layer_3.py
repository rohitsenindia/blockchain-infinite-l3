from eth_account import Account
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('YOUR_LAYER3_RPC_URL')) #Replace with your Layer 3 RPC URL

contract_abi = [
    {
        "inputs": [],
        "name": "getFee",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "uint256", "name": "_fee", "type": "uint256"}],
        "name": "setFee",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract_address = 'YOUR_CONTRACT_ADDRESS' #Replace with your deployed contract address

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

current_fee = contract.functions.getFee().call()
print(f"Current Fee: {current_fee}")

new_fee = 100 #Example new fee
txn = contract.functions.setFee(new_fee).buildTransaction({
    'chainId': w3.eth.chain_id,
    'gas': 1000000,
    'gasPrice': w3.eth.gas_price,
    'nonce': w3.eth.getTransactionCount('YOUR_ACCOUNT_ADDRESS') #Replace with your account address
})

private_key = 'YOUR_PRIVATE_KEY' #Replace with your private key
signed_txn = w3.eth.account.signTransaction(txn, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(f"Transaction Hash: {tx_hash.hex()}")

receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f"Transaction Receipt: {receipt}")

updated_fee = contract.functions.getFee().call()
print(f"Updated Fee: {updated_fee}")
