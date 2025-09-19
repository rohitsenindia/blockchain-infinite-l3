from web3 import Web3

class Layer1Interop:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract_address = '0xYOUR_CONTRACT_ADDRESS' # Replace with actual contract address
        self.contract_abi = [{'constant': True, 'inputs': [], 'name': 'someFunction', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}] #Replace with actual ABI
        try:
            self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        except Exception as e:
            raise ValueError(f"Failed to connect to Layer 1 contract: {e}")


    def get_data(self):
        try:
            data = self.contract.functions.someFunction().call()
            return data
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve data from Layer 1: {e}")

    def send_transaction(self, private_key, function_name, *args):
        nonce = self.w3.eth.getTransactionCount(self.w3.toChecksumAddress('YOUR_ACCOUNT_ADDRESS')) #Replace with actual account address
        txn = self.contract.functions[function_name](*args).buildTransaction({
            'chainId': 1, #Replace with your chain ID
            'gas': 1000000, #Adjust as needed
            'nonce': nonce,
            'from': 'YOUR_ACCOUNT_ADDRESS' #Replace with actual account address
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key=private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.toHex(tx_hash)

    def is_connected(self):
      return self.w3.isConnected()

