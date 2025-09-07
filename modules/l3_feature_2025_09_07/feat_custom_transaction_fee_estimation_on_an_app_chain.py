import math

def estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, priority_fee_gwei=0):
    gas_limit = math.ceil(tx_size_bytes / 1024) * 21000 # Assume 21k gas per KB
    total_gas_fee_gwei = gas_limit * gas_price_gwei
    priority_fee_total_gwei = gas_limit * priority_fee_gwei
    total_fee_gwei = total_gas_fee_gwei + priority_fee_total_gwei + base_fee_gwei
    return total_fee_gwei

def estimate_tx_fee_wei(tx_size_bytes, base_fee_gwei, gas_price_gwei, priority_fee_gwei=0):
    fee_gwei = estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, priority_fee_gwei)
    return fee_gwei * 10**9


def get_fee_in_eth(wei):
    return wei / 10**18

tx_size = 1024  # Example transaction size in bytes
base_fee = 10  #Example Base fee in Gwei
gas_price = 20 #Example Gas price in Gwei
priority_fee = 2 #Example Priority fee in Gwei

estimated_fee_gwei = estimate_tx_fee(tx_size, base_fee, gas_price, priority_fee)
estimated_fee_wei = estimate_tx_fee_wei(tx_size, base_fee, gas_price, priority_fee)
estimated_fee_eth = get_fee_in_eth(estimated_fee_wei)

print(f"Estimated Fee (Gwei): {estimated_fee_gwei}")
print(f"Estimated Fee (Wei): {estimated_fee_wei}")
print(f"Estimated Fee (ETH): {estimated_fee_eth}")
