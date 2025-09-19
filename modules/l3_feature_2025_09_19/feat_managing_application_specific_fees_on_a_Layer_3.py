from eth_typing import Address

class FeeManager:
    def __init__(self, owner: Address, fee_amount: int):
        self.owner = owner
        self.fee_amount = fee_amount
        self.total_fees_collected = 0

    def set_fee(self, new_fee_amount: int):
        if msg.sender != self.owner:
            raise Exception("Only the owner can set the fee amount.")
        self.fee_amount = new_fee_amount

    def pay_fee(self):
        if msg.value < self.fee_amount:
            raise Exception("Insufficient fee amount.")
        self.total_fees_collected += self.fee_amount
        send(self.owner, self.fee_amount)

    def get_total_fees(self) -> int:
        return self.total_fees_collected

    def withdraw_fees(self):
        if msg.sender != self.owner:
            raise Exception("Only the owner can withdraw fees.")
        amount_to_withdraw = self.total_fees_collected
        self.total_fees_collected = 0
        send(self.owner, amount_to_withdraw)

    def get_fee_amount(self) -> int:
        return self.fee_amount

