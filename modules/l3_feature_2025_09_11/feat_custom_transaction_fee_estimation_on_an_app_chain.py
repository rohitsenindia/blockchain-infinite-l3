from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_multiplier=1.0, congestion_factor=1.0):
    base_fee = Decimal(tx_size_bytes) * Decimal(base_fee_per_byte)
    priority_fee = base_fee * Decimal(priority_multiplier)
    congestion_fee = base_fee * Decimal(congestion_factor)
    total_fee = base_fee + priority_fee + congestion_fee
    return total_fee.quantize(Decimal("0.00000001"))

# Example usage
tx_size = 1024  # bytes
base_fee_rate = Decimal("0.000001") # Example rate in your app-chain's currency per byte
priority = 1.5 # Higher for faster confirmation
congestion = 1.2 # Higher during network congestion

estimated_fee = estimate_tx_fee(tx_size, base_fee_rate, priority, congestion)
print(f"Estimated transaction fee: {estimated_fee}")

