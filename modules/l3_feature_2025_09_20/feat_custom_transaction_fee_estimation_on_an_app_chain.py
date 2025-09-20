import math

class FeeEstimator:
    def __init__(self, base_fee, gas_price_per_unit, size_factor):
        self.base_fee = base_fee
        self.gas_price_per_unit = gas_price_per_unit
        self.size_factor = size_factor

    def estimate_fee(self, transaction_size_bytes):
        gas_fee = math.ceil(transaction_size_bytes * self.size_factor) * self.gas_price_per_unit
        total_fee = self.base_fee + gas_fee
        return total_fee

    def estimate_fee_with_priority(self, transaction_size_bytes, priority_factor):
        gas_fee = math.ceil(transaction_size_bytes * self.size_factor * priority_factor) * self.gas_price_per_unit
        total_fee = self.base_fee + gas_fee
        return total_fee

estimator = FeeEstimator(base_fee=10, gas_price_per_unit=0.00001, size_factor=0.001)
transaction_size = 1024
estimated_fee = estimator.estimate_fee(transaction_size)
priority_fee = estimator.estimate_fee_with_priority(transaction_size, 1.5)
print(f"Estimated fee: {estimated_fee}")
print(f"Estimated fee with priority: {priority_fee}")

