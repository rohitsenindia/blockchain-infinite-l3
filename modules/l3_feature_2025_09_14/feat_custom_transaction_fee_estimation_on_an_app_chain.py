from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_multiplier=1.0):
    priority_fee_per_byte = Decimal(base_fee_per_byte) * Decimal(priority_multiplier)
    total_fee = (Decimal(tx_size_bytes) * priority_fee_per_byte).quantize(Decimal("0.00000001"))
    return total_fee

def get_base_fee(app_chain_id):
    # Replace with actual fee retrieval from chain state or config
    base_fees = {
        1: Decimal("0.0000001"),
        2: Decimal("0.0000002"),
    }
    return base_fees.get(app_chain_id, Decimal("0.0000001"))  # Default base fee


def estimate_custom_tx_fee(tx_size_bytes, app_chain_id, priority_multiplier=1.0):
    base_fee = get_base_fee(app_chain_id)
    return estimate_tx_fee(tx_size_bytes, base_fee, priority_multiplier)


tx_size = 1024  # Example transaction size in bytes
app_chain = 1   # Example app chain ID
priority = 1.5  # Example priority multiplier (higher for faster confirmation)

estimated_fee = estimate_custom_tx_fee(tx_size, app_chain, priority)
print(f"Estimated transaction fee: {estimated_fee}")

