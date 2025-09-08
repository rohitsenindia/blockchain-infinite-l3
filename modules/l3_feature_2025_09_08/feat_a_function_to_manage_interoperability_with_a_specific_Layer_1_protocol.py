import requests

def interact_with_solana(endpoint, method, params=None):
    headers = {'Content-Type': 'application/json'}
    url = f"{endpoint}{method}"
    if method == '/tx':
        response = requests.post(url, headers=headers, json=params)
    elif method == '/account':
        response = requests.get(url, headers=headers, params=params)
    else:
        return {"error": "unsupported method"}

    if response.status_code >= 200 and response.status_code < 300:
        try:
            return response.json()
        except:
            return {"error": "invalid json response"}
    else:
        return {"error": response.text}


def get_solana_balance(endpoint, publicKey):
    result = interact_with_solana(endpoint, '/account', {'publicKey': publicKey})
    if 'error' in result:
        return 0
    else:
        return int(result['result']['lamports'])


def send_solana_transaction(endpoint, transaction):
    result = interact_with_solana(endpoint, '/tx', {'transaction': transaction})
    return result


