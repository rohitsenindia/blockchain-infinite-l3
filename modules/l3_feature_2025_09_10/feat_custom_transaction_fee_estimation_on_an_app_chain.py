from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, priority_multiplier=1.0, congestion_factor=1.0):
    base_fee = Decimal(tx_size_bytes) * Decimal(base_fee_per_byte)
    priority_fee = base_fee * Decimal(priority_multiplier)
    congestion_fee = base_fee * Decimal(congestion_factor)
    total_fee = base_fee + priority_fee + congestion_fee
    return total_fee.quantize(Decimal("0.00000001"))


def get_congestion_factor(network_utilization):
    if network_utilization > 0.9:
        return Decimal("2.0")
    elif network_utilization > 0.7:
        return Decimal("1.5")
    else:
        return Decimal("1.0")


tx_size = 1024  # bytes
base_fee = 0.000001 # per byte
network_utilization = 0.8
priority = 1.2 # priority multiplier


congestion = get_congestion_factor(network_utilization)
estimated_fee = estimate_tx_fee(tx_size, base_fee, priority, congestion)
print(f"Estimated Transaction Fee: {estimated_fee}")

