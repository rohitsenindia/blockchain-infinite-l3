from web3 import Web3

class Layer1Interop:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def get_balance(self, address):
        return self.contract.functions.getBalance(address).call()

    def transfer_tokens(self, to_address, amount, private_key):
        nonce = self.w3.eth.getTransactionCount(self.w3.toChecksumAddress(self.w3.eth.accounts[0]))
        txn = self.contract.functions.transfer(to_address, amount).buildTransaction({
            'chainId': self.w3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.toHex(tx_hash)

    def get_token_name(self):
        return self.contract.functions.name().call()
