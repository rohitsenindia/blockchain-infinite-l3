import math

def estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, network_congestion=1.0):
    gas_limit = math.ceil(tx_size_bytes / 1024) * 21000 # Example gas limit estimation
    gas_price = gas_price_gwei * network_congestion
    fee_gwei = gas_limit * gas_price
    total_fee_gwei = fee_gwei + base_fee_gwei
    return total_fee_gwei

def estimate_tx_fee_wei(tx_size_bytes, base_fee_gwei, gas_price_gwei, network_congestion=1.0):
    total_fee_gwei = estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, network_congestion)
    return total_fee_gwei * 10**9

tx_size = 1024
base_fee = 10
gas_price = 20
congestion = 1.5

estimated_fee_gwei = estimate_tx_fee(tx_size, base_fee, gas_price, congestion)
estimated_fee_wei = estimate_tx_fee_wei(tx_size, base_fee, gas_price, congestion)

print(f"Estimated transaction fee (GWEI): {estimated_fee_gwei}")
print(f"Estimated transaction fee (WEI): {estimated_fee_wei}")
