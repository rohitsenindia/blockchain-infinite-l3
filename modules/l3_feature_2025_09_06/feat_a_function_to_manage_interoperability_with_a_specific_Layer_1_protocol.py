import requests

def interact_with_solana(action, params):
    url = "https://api.mainnet-beta.solana.com"  
    headers = {'Content-Type': 'application/json'}
    if action == "get_balance":
        response = requests.get(f"{url}/account/{params['address']}", headers=headers)
        return response.json()
    elif action == "send_transaction":
        response = requests.post(f"{url}", json=params, headers=headers)
        return response.json()
    else:
        return {"error": "Unsupported action"}

def process_solana_response(response):
    if 'result' in response:
        return response['result']
    elif 'error' in response:
        raise Exception(f"Solana API Error: {response['error']}")
    else:
        raise Exception("Unexpected response from Solana API")

def solana_interop(action, *args, **kwargs):
  try:
    params = kwargs.get('params', {})
    response = interact_with_solana(action, params)
    return process_solana_response(response)
  except requests.exceptions.RequestException as e:
    raise Exception(f"Network error interacting with Solana: {e}")
  except Exception as e:
    raise Exception(f"Error during Solana interaction: {e}")

