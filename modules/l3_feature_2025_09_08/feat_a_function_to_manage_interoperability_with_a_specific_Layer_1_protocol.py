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
            "private_key": private_key
        }
        response = requests.post(f"{self.api_url}/transaction", json=payload)
        response.raise_for_status()
        return response.json()['transaction_hash']

    def get_transaction_status(self, transaction_hash):
        response = requests.get(f"{self.api_url}/transaction/{transaction_hash}")
        response.raise_for_status()
        return response.json()['status']
