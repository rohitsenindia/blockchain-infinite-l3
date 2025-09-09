import requests

class Layer1Interop:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_balance(self, address):
        url = f"{self.api_url}/balance/{address}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['balance']

    def send_transaction(self, from_address, to_address, amount, private_key):
        url = f"{self.api_url}/transaction"
        payload = {
            "from": from_address,
            "to": to_address,
            "amount": amount,
            "signature": self._sign_transaction(private_key, from_address, to_address, amount)
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()['transaction_hash']

    def _sign_transaction(self, private_key, from_address, to_address, amount):
        # Placeholder for actual signing logic using private_key
        # This would typically involve elliptic curve cryptography
        return "0xsignedtransaction" 
