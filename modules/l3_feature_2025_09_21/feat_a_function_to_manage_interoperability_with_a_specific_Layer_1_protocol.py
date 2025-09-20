import requests

class Layer1Interop:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_balance(self, address):
        response = requests.get(f"{self.api_url}/balance/{address}")
        response.raise_for_status()
        return response.json()['balance']

    def send_transaction(self, from_address, to_address, amount, private_key):
        payload = {
            "from": from_address,
            "to": to_address,
            "amount": amount,
            "signature": self._sign_transaction(private_key, from_address, to_address, amount)
        }
        response = requests.post(f"{self.api_url}/transaction", json=payload)
        response.raise_for_status()
        return response.json()['transaction_hash']

    def _sign_transaction(self, private_key, from_address, to_address, amount):
        # Placeholder for actual signing logic using private_key, replace with your Layer 1's signing mechanism.
        #  This is crucial for security;  Do NOT use this placeholder in production.
        return "mock_signature"

    def get_transaction_receipt(self, transaction_hash):
        response = requests.get(f"{self.api_url}/transaction/{transaction_hash}")
        response.raise_for_status()
        return response.json()

    def get_block(self, block_number):
        response = requests.get(f"{self.api_url}/block/{block_number}")
        response.raise_for_status()
        return response.json()

