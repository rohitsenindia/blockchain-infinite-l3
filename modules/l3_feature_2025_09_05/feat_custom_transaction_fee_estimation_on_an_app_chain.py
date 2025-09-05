from decimal import Decimal

def estimate_tx_fee(tx_size_bytes, base_fee_per_byte, gas_used, gas_price_gwei):
    byte_fee = Decimal(tx_size_bytes) * Decimal(base_fee_per_byte)
    gas_fee_eth = Decimal(gas_used) * Decimal(gas_price_gwei) / Decimal(10**9)
    total_fee_eth = byte_fee + gas_fee_eth
    return total_fee_eth

def get_estimated_fee(tx_size, base_fee, gas_used, gas_price):
    return estimate_tx_fee(tx_size, base_fee, gas_used, gas_price)


tx_size_bytes = 1024  # Example transaction size in bytes
base_fee_per_byte = 0.00000001 # Example base fee in ETH per byte
gas_used = 21000 # Example gas used
gas_price_gwei = 10 # Example gas price in GWEI

estimated_fee = get_estimated_fee(tx_size_bytes, base_fee_per_byte, gas_used, gas_price_gwei)

print(f"Estimated transaction fee: {estimated_fee:.8f} ETH")
