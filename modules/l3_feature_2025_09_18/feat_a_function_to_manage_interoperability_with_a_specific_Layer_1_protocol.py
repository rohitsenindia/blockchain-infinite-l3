import requests

def interact_with_solana(action, params={}):
    url = "https://api.mainnet-beta.solana.com"  
    if action == "getBalance":
        response = requests.get(f"{url}/account/{params['address']}")
        return response.json()['result']['lamports']
    elif action == "sendTransaction":
        response = requests.post(f"{url}", json=params)
        return response.json()
    else:
        return {"error": "Unsupported action"}

#Example Usage
balance = interact_with_solana("getBalance", {"address": "YOUR_SOLANA_ADDRESS"})
print(f"Balance: {balance}")

transaction_result = interact_with_solana("sendTransaction", {"transaction": "YOUR_SOLANA_TRANSACTION"})
print(f"Transaction Result: {transaction_result}")

