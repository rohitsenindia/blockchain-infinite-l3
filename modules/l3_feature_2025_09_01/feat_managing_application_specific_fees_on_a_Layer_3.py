from eth_utils import to_wei

class FeeManager:
    def __init__(self, initial_fee_rate=to_wei(0.01, 'ether')):
        self.fee_rate = initial_fee_rate
        self.total_fees_collected = 0

    def set_fee_rate(self, new_fee_rate):
        # Requires authorization check in a real implementation.
        self.fee_rate = new_fee_rate

    def get_fee_rate(self):
        return self.fee_rate

    def pay_fee(self, amount):
        fee_amount = amount * self.fee_rate / to_wei(1, 'ether')
        #Requires transaction processing logic to transfer fee amount.
        self.total_fees_collected += fee_amount
        return fee_amount

    def get_total_fees_collected(self):
        return self.total_fees_collected

#Example usage:
fee_manager = FeeManager()
fee = fee_manager.pay_fee(to_wei(10, 'ether'))
print(f"Fee paid: {fee}")
new_rate = to_wei(0.02, 'ether')
fee_manager.set_fee_rate(new_rate)
fee2 = fee_manager.pay_fee(to_wei(5, 'ether'))
print(f"Fee paid after rate change: {fee2}")
print(f"Total fees collected: {fee_manager.get_total_fees_collected()}")

