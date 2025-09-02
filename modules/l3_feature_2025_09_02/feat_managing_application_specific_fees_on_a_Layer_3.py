from eth_typing import Address
from web3 import Web3

class FeeManager:
    def __init__(self, w3: Web3, contract_address: Address, abi):
        self.w3 = w3
        self.contract = w3.eth.contract(address=contract_address, abi=abi)

    def set_fee(self, fee_amount: int):
        txn = self.contract.functions.setFee(fee_amount).buildTransaction({
            'from': self.w3.eth.accounts[0],
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.accounts[0])
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key='YOUR_PRIVATE_KEY')
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash

    def get_fee(self) -> int:
        return self.contract.functions.fee().call()

    def pay_fee(self, payer_address: Address):
        txn = self.contract.functions.payFee(payer_address).buildTransaction({
            'from': payer_address,
            'nonce': self.w3.eth.getTransactionCount(payer_address),
            'value': self.get_fee()
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key='YOUR_PRIVATE_KEY') #Replace with payer's private key in production
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash

# Example usage (replace with your actual values)
w3 = Web3(Web3.HTTPProvider('YOUR_PROVIDER_URL'))
contract_address = 'YOUR_CONTRACT_ADDRESS'
abi = [{'inputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [], 'name': 'fee', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_fee', 'type': 'uint256'}], 'name': 'setFee', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'payer', 'type': 'address'}], 'name': 'payFee', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}]


fee_manager = FeeManager(w3, contract_address, abi)
#fee_manager.set_fee(1000000000000000) # 0.01 ETH
#fee = fee_manager.get_fee()
#print(f"Current Fee: {fee}")
#fee_manager.pay_fee('YOUR_PAYER_ADDRESS')

