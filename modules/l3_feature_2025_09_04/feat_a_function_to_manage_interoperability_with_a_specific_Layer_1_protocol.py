from eth_account import Account
from web3 import Web3

def interact_with_ethereum(private_key, contract_address, abi, function_name, *args):
    w3 = Web3(Web3.HTTPProvider('YOUR_ETHEREUM_NODE_URL'))
    account = Account.from_key(private_key)
    contract = w3.eth.contract(address=contract_address, abi=abi)
    nonce = w3.eth.getTransactionCount(account.address)
    transaction = contract.functions[function_name](*args).buildTransaction({
        'chainId': 1,  # Replace with appropriate chain ID
        'gas': 5000000, # Adjust as needed
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.signTransaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

# Example usage (replace with your actual values):
private_key = 'YOUR_PRIVATE_KEY'
contract_address = 'YOUR_CONTRACT_ADDRESS'
abi = [{'inputs': [], 'name': 'myFunction', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'pure', 'type': 'function'}]
receipt = interact_with_ethereum(private_key, contract_address, abi, 'myFunction')
print(receipt)

