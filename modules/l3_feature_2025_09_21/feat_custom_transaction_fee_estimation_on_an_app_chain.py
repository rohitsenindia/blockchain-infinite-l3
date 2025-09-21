import math

def estimate_tx_fee(tx_size_bytes, base_fee_gwei, gas_price_gwei, gas_limit_gwei=None):
    if gas_limit_gwei is None:
        gas_limit_gwei = max(1, math.ceil(tx_size_bytes / 1024)) #Estimate gas limit based on size

    gas_fee_gwei = gas_limit_gwei * gas_price_gwei
    total_fee_gwei = base_fee_gwei + gas_fee_gwei
    return total_fee_gwei

def gwei_to_wei(gwei):
    return gwei * 10**9

tx_size = 1500 # bytes
base_fee = 10 # gwei
gas_price = 2 # gwei

estimated_fee_gwei = estimate_tx_fee(tx_size, base_fee, gas_price)
estimated_fee_wei = gwei_to_wei(estimated_fee_gwei)

print(f"Estimated Transaction Fee: {estimated_fee_gwei} GWEI ({estimated_fee_wei} WEI)")

