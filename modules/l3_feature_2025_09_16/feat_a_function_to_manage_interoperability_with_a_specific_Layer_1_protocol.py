import requests

class Layer1Bridge:
    def __init__(self, api_url):
        self.api_url = api_url

    def transfer_tokens(self, recipient_address, amount, token_id):
        headers = {'Content-Type': 'application/json'}
        payload = {
            'recipient': recipient_address,
            'amount': amount,
            'token_id': token_id
        }
        response = requests.post(f"{self.api_url}/transfer", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_balance(self, address, token_id):
        response = requests.get(f"{self.api_url}/balance/{address}/{token_id}")
        response.raise_for_status()
        return response.json()['balance']

    def get_transaction_status(self, transaction_id):
        response = requests.get(f"{self.api_url}/transaction/{transaction_id}")
        response.raise_for_status()
        return response.json()['status']
