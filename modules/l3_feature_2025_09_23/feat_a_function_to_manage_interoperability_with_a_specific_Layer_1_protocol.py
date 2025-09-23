import requests

class Layer1Interop:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_balance(self, address):
        response = requests.get(f"{self.api_url}/balance/{address}")
        response.raise_for_status()
        return response.json()["balance"]

    def send_transaction(self, sender, recipient, amount, private_key):
        payload = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "signature": self._sign_transaction(private_key, sender, recipient, amount)
        }
        response = requests.post(f"{self.api_url}/transaction", json=payload)
        response.raise_for_status()
        return response.json()["transaction_hash"]

    def _sign_transaction(self, private_key, sender, recipient, amount):
        # Replace with actual signing logic using appropriate library
        # This is a placeholder
        return "mock_signature"

    def get_transaction_receipt(self, transaction_hash):
        response = requests.get(f"{self.api_url}/transaction/{transaction_hash}")
        response.raise_for_status()
        return response.json()

    def get_block_by_height(self, block_height):
      response = requests.get(f"{self.api_url}/block/{block_height}")
      response.raise_for_status()
      return response.json()
