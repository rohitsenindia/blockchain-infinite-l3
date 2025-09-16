from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_factor=1.0):
    priority_fee = base_fee_per_byte * Decimal(priority_factor)
    total_fee = (base_fee_per_byte + priority_fee) * tx_size_bytes
    return total_fee.quantize(Decimal("0.00000001"))

def get_base_fee():
    # Replace with actual base fee retrieval mechanism from app-chain
    # e.g., fetching from a node API
    return Decimal("0.0000001")

tx_size = 1024  # Example transaction size in bytes
base_fee = get_base_fee()
estimated_fee = estimate_tx_fee(tx_size, base_fee, priority_factor=1.5)
print(f"Estimated transaction fee: {estimated_fee}")

high_priority_fee = estimate_tx_fee(tx_size, base_fee, priority_factor=3.0)
print(f"Estimated high-priority transaction fee: {high_priority_fee}")

low_priority_fee = estimate_tx_fee(tx_size, base_fee, priority_factor=0.5)
print(f"Estimated low-priority transaction fee: {low_priority_fee}")
