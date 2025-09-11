from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_multiplier=1.0):
    base_fee = Decimal(tx_size_bytes) * Decimal(base_fee_per_byte)
    priority_fee = base_fee * Decimal(priority_multiplier - 1) if priority_multiplier > 1 else 0
    total_fee = base_fee + priority_fee
    return total_fee.quantize(Decimal("0.00000001"))

def get_base_fee(app_chain_id):
    # Replace with actual fee retrieval from app-chain
    fee_data = {
        1: Decimal("0.000001"),
        2: Decimal("0.000002"),
    }
    return fee_data.get(app_chain_id, Decimal("0.000001"))

app_chain_id = 1
tx_size = 1024  # bytes
priority = 1.5 # Multiplier for priority transactions

base_fee_per_byte = get_base_fee(app_chain_id)
estimated_fee = estimate_tx_fee(tx_size, base_fee_per_byte, priority)

print(f"Estimated transaction fee: {estimated_fee}")

