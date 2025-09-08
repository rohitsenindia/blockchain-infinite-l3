from web3 import Web3

class Layer1Interoperability:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.w3.isConnected():
            raise ConnectionError("Failed to connect to Layer 1 provider.")

    def get_balance(self, address):
        return self.w3.eth.getBalance(address)

    def send_transaction(self, to_address, value, private_key, nonce=None):
        if nonce is None:
            nonce = self.w3.eth.getTransactionCount(self.w3.eth.defaultAccount)
        txn = {
            'nonce': nonce,
            'to': to_address,
            'value': value,
            'gas': 21000,
            'gasPrice': self.w3.eth.gasPrice
        }
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key)
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def get_block_number(self):
        return self.w3.eth.blockNumber

    def set_default_account(self, address):
        self.w3.eth.defaultAccount = address
