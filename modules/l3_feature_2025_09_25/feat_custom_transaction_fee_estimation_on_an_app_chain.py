from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, gas_price_gwei, gas_limit):
    base_fee = Decimal(tx_size_bytes) * Decimal(base_fee_per_byte)
    gas_fee = Decimal(gas_price_gwei) * Decimal(gas_limit) / Decimal(10**9)
    total_fee = base_fee + gas_fee
    return total_fee.quantize(Decimal("0.00000001"))


def main():
    tx_size = 1024  # bytes
    base_fee = 0.0000001 # per byte
    gas_price = 10 # gwei
    gas_limit = 21000
    estimated_fee = estimate_tx_fee(tx_size, base_fee, gas_price, gas_limit)
    print(f"Estimated transaction fee: {estimated_fee}")


if __name__ == "__main__":
    main()
