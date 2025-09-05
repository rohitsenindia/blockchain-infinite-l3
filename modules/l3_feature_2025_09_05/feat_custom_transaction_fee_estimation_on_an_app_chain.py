from typing import Dict, Tuple

def estimate_transaction_fee(transaction: Dict, base_fee: float, gas_prices: Dict[str, float]) -> float:
    gas_used = transaction['gasUsed']
    gas_price_per_unit = gas_prices.get(transaction['gasType'], base_fee)
    return gas_used * gas_price_per_unit


def get_gas_prices(api_url: str) -> Dict[str, float]:
    # Simulate fetching gas prices from an API; replace with actual API call
    mock_gas_prices = {'fast': 0.0001, 'average': 0.00008, 'slow': 0.00005}
    return mock_gas_prices

def main():
    transaction = {'gasUsed': 100000, 'gasType': 'average'}
    base_fee = 0.00005
    gas_prices = get_gas_prices("https://example.com/gasprices")
    fee = estimate_transaction_fee(transaction, base_fee, gas_prices)
    print(f"Estimated transaction fee: {fee}")


if __name__ == "__main__":
    main()
