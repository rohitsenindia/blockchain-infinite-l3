from eth_typing import Address
from web3 import Web3

class FeeManager:
    def __init__(self, w3: Web3, contract_address: Address):
        self.w3 = w3
        self.contract = self.w3.eth.contract(address=contract_address, abi=self.get_abi())

    def get_abi(self):
        return [
            {
                "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
                "name": "setFee",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "getFee",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function",
            },
        ]

    def set_fee(self, amount: int):
        txn = self.contract.functions.setFee(amount).buildTransaction({
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.defaultAccount),
            'gas': 1000000,
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key=self.w3.eth.defaultAccount)
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return tx_hash

    def get_fee(self) -> int:
        return self.contract.functions.getFee().call()
