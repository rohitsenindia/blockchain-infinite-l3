from web3 import Web3

class Layer1Bridge:
    def __init__(self, provider_url, contract_address, abi):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.w3.eth.contract(address=contract_address, abi=abi)

    def get_token_balance(self, address, token_address=None):
        if token_address:
            return self.contract.functions.balanceOf(address, token_address).call()
        else:
            return self.contract.functions.balanceOf(address).call()

    def transfer_tokens(self, recipient, amount, token_address=None, private_key=None):
        nonce = self.w3.eth.getTransactionCount(self.w3.eth.accounts[0])
        if token_address:
            tx = self.contract.functions.transfer(recipient, amount, token_address).buildTransaction({
                'chainId': self.w3.eth.chain_id,
                'gas': 1000000,
                'gasPrice': self.w3.eth.gasPrice,
                'nonce': nonce,
            })
        else:
            tx = self.contract.functions.transfer(recipient, amount).buildTransaction({
                'chainId': self.w3.eth.chain_id,
                'gas': 1000000,
                'gasPrice': self.w3.eth.gasPrice,
                'nonce': nonce,
            })
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.w3.toHex(tx_hash)
