from eth_utils import to_wei

class FeeManager:
    def __init__(self, l3_client, fee_token_address):
        self.l3_client = l3_client
        self.fee_token_address = fee_token_address

    def set_fee(self, amount, currency="ETH"):
        amount_wei = to_wei(amount, currency)
        self.l3_client.send_transaction({
            'to': self.fee_token_address,
            'value': amount_wei,
            'data': b'\x00' # Placeholder for function signature
        })

    def get_fee(self):
        balance = self.l3_client.get_balance(self.fee_token_address)
        return balance


    def pay_fee(self, amount, currency="ETH", payer_address=None):
        amount_wei = to_wei(amount, currency)
        if not payer_address:
          payer_address = self.l3_client.account.address
        self.l3_client.send_transaction({
            'from': payer_address,
            'to': self.fee_token_address,
            'value': amount_wei
        })
        return True

    def check_sufficient_funds(self, amount, currency="ETH", payer_address=None):
      if not payer_address:
        payer_address = self.l3_client.account.address
      balance = self.l3_client.get_balance(payer_address, currency)
      amount_wei = to_wei(amount, currency)
      return balance >= amount_wei
