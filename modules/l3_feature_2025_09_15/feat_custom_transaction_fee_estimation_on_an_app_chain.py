from decimal import Decimal

class FeeEstimator:
    def __init__(self, base_fee: Decimal, byte_fee: Decimal, gas_multiplier: Decimal = Decimal(1.2)):
        self.base_fee = base_fee
        self.byte_fee = byte_fee
        self.gas_multiplier = gas_multiplier

    def estimate_fee(self, transaction_bytes: int, gas_used: int) -> Decimal:
        gas_fee = self.base_fee + (gas_used * self.byte_fee * self.gas_multiplier)
        return gas_fee

    def estimate_transaction_fee(self, tx_size_bytes: int) -> Decimal:
        return self.base_fee + (tx_size_bytes * self.byte_fee)


estimator = FeeEstimator(base_fee=Decimal('0.0001'), byte_fee=Decimal('0.000001'))
transaction_fee = estimator.estimate_transaction_fee(1024)
print(f"Estimated Transaction Fee: {transaction_fee}")

gas_fee = estimator.estimate_fee(1024, 10000)
print(f"Estimated Gas Fee: {gas_fee}")
