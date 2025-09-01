import math

def estimate_tx_fee(tx_size_bytes, base_fee, gas_price_gwei, gas_limit=None):
    if gas_limit is None:
        gas_limit = tx_size_bytes * 21  # Assume 21 gas per byte, adjust as needed
    gas_fee_gwei = gas_limit * gas_price_gwei
    gas_fee_wei = gas_fee_gwei * 10**9
    total_fee_wei = gas_fee_wei + base_fee
    total_fee_eth = total_fee_wei / 10**18
    return math.ceil(total_fee_eth * 10**18) / 10**18

def estimate_tx_size(num_inputs, num_outputs, data_size_bytes):
    return 100 + (num_inputs * 148) + (num_outputs * 32) + data_size_bytes #Example values, adjust as per your app chain's specifications.

base_fee = 10**17 #Example Base Fee in wei
gas_price_gwei = 20 # Example gas price in Gwei

num_inputs = 2
num_outputs = 3
data_size_bytes = 1000

tx_size = estimate_tx_size(num_inputs, num_outputs, data_size_bytes)
estimated_fee = estimate_tx_fee(tx_size, base_fee, gas_price_gwei)

print(f"Estimated transaction size: {tx_size} bytes")
print(f"Estimated transaction fee: {estimated_fee} wei")

