from eth_typing import Address
from web3 import Web3

class FeeManager:
    def __init__(self, w3: Web3, contract_address: Address):
        self.w3 = w3
        self.contract = self.w3.eth.contract(address=contract_address, abi=[
            {'inputs': [{'internalType': 'uint256', 'name': '_feeAmount', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'},
            {'inputs': [], 'name': 'getFee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}
        ])

    def set_fee(self, fee_amount: int, private_key: str):
        txn = self.contract.functions.setFee(fee_amount).buildTransaction({
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.accounts[0]),
            'gas': 1000000,
            'gasPrice': self.w3.eth.gas_price
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key=private_key)
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.w3.eth.waitForTransactionReceipt(txn_hash)

    def get_fee(self) -> int:
        return self.contract.functions.getFee().call()
