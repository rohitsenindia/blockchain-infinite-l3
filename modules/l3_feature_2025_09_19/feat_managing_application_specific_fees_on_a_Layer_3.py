from eth_typing import Address, ChecksumAddress
from web3 import Web3

class FeeManager:
    def __init__(self, w3: Web3, contract_address: ChecksumAddress):
        self.w3 = w3
        with open('fee_manager_abi.json', 'r') as f:
            abi = json.load(f)
        self.contract = w3.eth.contract(address=contract_address, abi=abi)

    def set_fee(self, new_fee: int):
        tx_hash = self.contract.functions.setFee(new_fee).transact({'from': self.w3.eth.accounts[0]})
        self.w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_hash

    def get_fee(self) -> int:
        return self.contract.functions.getFee().call()

    def pay_fee(self, payer: Address) -> str:
      tx_hash = self.contract.functions.payFee().transact({'from': payer})
      self.w3.eth.waitForTransactionReceipt(tx_hash)
      return tx_hash

    def get_fee_balance(self) -> int:
      return self.contract.functions.getFeeBalance().call()


import json
# ... (Assume w3 instance and contract address are available) ...
fee_manager = FeeManager(w3, contract_address)
new_fee = 10**18 # 1 ETH
fee_manager.set_fee(new_fee)
current_fee = fee_manager.get_fee()
print(f"Current fee: {current_fee}")
payer_address = "0x..." # Replace with a valid address
fee_manager.pay_fee(payer_address)
balance = fee_manager.get_fee_balance()
print(f"Fee balance: {balance}")

