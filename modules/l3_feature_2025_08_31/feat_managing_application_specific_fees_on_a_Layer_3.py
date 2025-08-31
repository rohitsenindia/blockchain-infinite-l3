from eth_typing import Address

class FeeManager:
    def __init__(self, owner: Address, fee_amount: int):
        self.owner = owner
        self.fee_amount = fee_amount
        self.collected_fees = 0

    def set_fee(self, new_fee_amount: int) -> bool:
        if msg.sender == self.owner:
            self.fee_amount = new_fee_amount
            return True
        return False
    
    def pay_fee(self) -> bool:
        if msg.value >= self.fee_amount:
            self.collected_fees += self.fee_amount
            send(msg.sender, msg.value - self.fee_amount)
            return True
        return False

    def withdraw_fees(self) -> bool:
        if msg.sender == self.owner:
            send(self.owner, self.collected_fees)
            self.collected_fees = 0
            return True
        return False
