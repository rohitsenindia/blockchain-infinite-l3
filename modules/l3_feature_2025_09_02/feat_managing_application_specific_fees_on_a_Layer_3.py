from eth_typing import Address
from web3 import Web3

class FeeManager:
    def __init__(self, w3: Web3, contract_address: Address):
        self.w3 = w3
        self.contract = self.w3.eth.contract(address=contract_address, abi=[
            {
                "inputs": [{"internalType": "uint256", "name": "_feeAmount", "type": "uint256"}],
                "name": "setFee",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "getFee",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function"
            }
        ])

    def set_fee(self, amount: int):
        txn = self.contract.functions.setFee(amount).buildTransaction({
            'chainId': self.w3.eth.chain_id,
            'gas': 1000000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.defaultAccount)
        })
        signed_txn = self.w3.eth.account.signTransaction(txn, private_key='YOUR_PRIVATE_KEY')
        tx_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        self.w3.eth.waitForTransactionReceipt(tx_hash)

    def get_fee(self) -> int:
        return self.contract.functions.getFee().call()

#Example Usage (Replace with your actual values)
#w3 = Web3(Web3.HTTPProvider('YOUR_RPC_URL'))
#fee_manager = FeeManager(w3, 'YOUR_CONTRACT_ADDRESS')
#fee_manager.set_fee(1000)
#current_fee = fee_manager.get_fee()
#print(f"Current fee: {current_fee}")

