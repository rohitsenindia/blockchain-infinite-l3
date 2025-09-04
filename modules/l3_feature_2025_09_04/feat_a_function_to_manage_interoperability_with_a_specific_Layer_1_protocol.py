import requests

class Layer1Interop:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_balance(self, address):
        response = requests.get(f"{self.api_url}/balance/{address}")
        response.raise_for_status()
        return response.json()["balance"]

    def send_transaction(self, sender, receiver, amount, private_key):
        payload = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "signature": self._sign_transaction(private_key, sender, receiver, amount)
        }
        response = requests.post(f"{self.api_url}/transaction", json=payload)
        response.raise_for_status()
        return response.json()["transaction_hash"]

    def _sign_transaction(self, private_key, sender, receiver, amount):
        # Replace with actual signing logic using appropriate library
        # This is a placeholder
        return "mock_signature"

    def get_transaction_status(self, transaction_hash):
        response = requests.get(f"{self.api_url}/transaction/{transaction_hash}")
        response.raise_for_status()
        return response.json()["status"]
