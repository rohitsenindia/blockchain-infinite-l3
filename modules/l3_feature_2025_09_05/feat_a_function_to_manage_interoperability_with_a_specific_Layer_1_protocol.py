from web3 import Web3

class Layer1Interop:
    def __init__(self, provider_url):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

    def get_block_number(self):
        return self.w3.eth.blockNumber

    def get_balance(self, address):
        return self.w3.eth.getBalance(address)

    def send_transaction(self, private_key, to_address, amount, nonce=None):
        account = self.w3.eth.account.privateKeyToAccount(private_key)
        tx = {
            'nonce': nonce or self.w3.eth.getTransactionCount(account.address),
            'to': to_address,
            'value': amount,
            'gas': 21000,
            'gasPrice': self.w3.eth.gasPrice
        }
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def get_transaction_receipt(self, tx_hash):
        return self.w3.eth.getTransactionReceipt(tx_hash)

    def check_connection(self):
        return self.w3.isConnected()
