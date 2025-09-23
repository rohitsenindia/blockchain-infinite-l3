from web3 import Web3

class Layer1Bridge:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def transfer(self, recipient, amount):
        txn = self.contract.functions.transfer(recipient, amount).buildTransaction({
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.defaultAccount),
            'gas': 1000000,
            'gasPrice': self.w3.eth.gasPrice
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.toHex(tx_hash)

    def get_balance(self, address):
        return self.contract.functions.balanceOf(address).call()

    def get_allowance(self, owner, spender):
        return self.contract.functions.allowance(owner, spender).call()
