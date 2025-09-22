from web3 import Web3

class Layer1Interop:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def get_balance(self, address):
        return self.contract.functions.balanceOf(address).call()

    def transfer(self, to_address, amount, private_key):
        nonce = self.w3.eth.getTransactionCount(self.w3.toChecksumAddress(self.w3.eth.defaultAccount))
        transaction = {
            'nonce': nonce,
            'to': self.w3.toChecksumAddress(to_address),
            'value': amount,
            'gas': 2000000,
            'gasPrice': self.w3.eth.gasPrice,
        }
        signed_txn = self.w3.eth.account.signTransaction(transaction, private_key)
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.eth.waitForTransactionReceipt(txn_hash)

    def get_transaction_receipt(self, txn_hash):
        return self.w3.eth.getTransactionReceipt(txn_hash)


