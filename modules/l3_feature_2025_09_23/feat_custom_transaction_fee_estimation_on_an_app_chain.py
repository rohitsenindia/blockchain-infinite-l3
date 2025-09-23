from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_multiplier=1.0):
    priority_fee_per_byte = base_fee_per_byte * priority_multiplier
    total_fee = Decimal(tx_size_bytes) * Decimal(priority_fee_per_byte)
    return total_fee.quantize(Decimal("0.00000001"))

def get_base_fee(block_gas_used, block_gas_target, gas_price):
    gas_used_ratio = block_gas_used / block_gas_target if block_gas_target else 1.0
    base_fee = gas_price * gas_used_ratio
    return max(Decimal(base_fee), Decimal("0.00000001"))

# Example usage
block_gas_used = 10000000
block_gas_target = 15000000
gas_price = Decimal("0.0000001")
base_fee = get_base_fee(block_gas_used, block_gas_target, gas_price)
tx_size_bytes = 1000
estimated_fee = estimate_tx_fee(tx_size_bytes, base_fee, priority_multiplier=1.5)
print(f"Estimated transaction fee: {estimated_fee}")

