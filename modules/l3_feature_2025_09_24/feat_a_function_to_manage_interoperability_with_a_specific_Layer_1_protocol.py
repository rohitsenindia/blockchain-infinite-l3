import requests

class Layer1Interop:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_balance(self, address):
        response = requests.get(f"{self.api_url}/balance/{address}")
        response.raise_for_status()
        return response.json()["balance"]

    def send_transaction(self, from_address, to_address, amount, private_key):
        payload = {
            "from": from_address,
            "to": to_address,
            "amount": amount,
            "signature": self._sign_transaction(private_key, from_address, to_address, amount)
        }
        response = requests.post(f"{self.api_url}/transaction", json=payload)
        response.raise_for_status()
        return response.json()["tx_hash"]

    def _sign_transaction(self, private_key, from_address, to_address, amount):
        # Placeholder for actual signature generation; replace with appropriate library
        return f"signature_{private_key}_{from_address}_{to_address}_{amount}"

    def get_transaction_status(self, tx_hash):
        response = requests.get(f"{self.api_url}/transaction/{tx_hash}")
        response.raise_for_status()
        return response.json()["status"]
