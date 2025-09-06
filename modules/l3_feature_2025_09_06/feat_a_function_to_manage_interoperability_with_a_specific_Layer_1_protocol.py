from web3 import Web3

class Layer1Interop:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.w3.isConnected():
            raise ConnectionError("Failed to connect to Layer 1")

    def get_balance(self, address):
        return self.w3.eth.get_balance(address)

    def send_transaction(self, private_key, to_address, amount, gas=21000, gas_price=None):
        nonce = self.w3.eth.getTransactionCount(self.w3.toChecksumAddress(private_key))
        tx = {
            'nonce': nonce,
            'to': self.w3.toChecksumAddress(to_address),
            'value': amount,
            'gas': gas,
            'gasPrice': self.w3.eth.gasPrice if gas_price is None else gas_price,
        }
        signed_txn = self.w3.eth.account.signTransaction(tx, private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.toHex(tx_hash)

    def get_transaction_receipt(self, tx_hash):
        return self.w3.eth.getTransactionReceipt(tx_hash)
