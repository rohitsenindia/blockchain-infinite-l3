from eth_account import Account
from web3 import Web3

def interact_with_ethereum(private_key, contract_address, function_name, *args):
    try:
        account = Account.from_key(private_key)
        w3 = Web3(Web3.HTTPProvider('YOUR_INFURA_URL')) # Replace with your provider
        contract_abi =  [{"inputs":[],"name":"yourFunctionName","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}] #replace with your contract ABI
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        nonce = w3.eth.getTransactionCount(account.address)
        transaction = contract.functions[function_name](*args).buildTransaction({
            'chainId': 1,  # Replace with your chain ID
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce,
        })
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt
    except Exception as e:
        return {'error': str(e)}

