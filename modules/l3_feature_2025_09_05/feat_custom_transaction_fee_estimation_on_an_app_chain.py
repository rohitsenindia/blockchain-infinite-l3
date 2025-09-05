import math

def estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, priority_fee_gwei=0):
    gas_used = math.ceil(tx_size_bytes / 1024) + 21000  # Assume some base gas + gas per KB
    total_fee_gwei = (gas_used * gas_price_gwei) + priority_fee_gwei + base_fee_gwei
    return total_fee_gwei * 10**-9

def estimate_tx_fee_eth(tx_size_bytes, gas_price_gwei):
    return estimate_tx_fee(tx_size_bytes, 0, gas_price_gwei)


def estimate_tx_fee_custom(tx_size_bytes, base_fee_gwei, gas_price_multiplier=1.2):
    gas_price_gwei = base_fee_gwei * gas_price_multiplier
    return estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei)

tx_size = 1024 # example tx size in bytes
base_fee = 20 # gwei
gas_price = 50 # gwei


eth_fee = estimate_tx_fee_eth(tx_size, gas_price)
custom_fee = estimate_tx_fee_custom(tx_size, base_fee)

print(f"Estimated ETH transaction fee: {eth_fee:.6f} ETH")
print(f"Estimated custom transaction fee: {custom_fee:.6f} ETH")
