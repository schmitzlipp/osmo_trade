import requests


def transaction_success(hash: str):
    url = "https://rpc.osmosis.zone/tx"
    querystring = {"hash":"0x"+hash,"prove":"true"}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_dict = response.json()
        code = response_dict["result"]["tx_result"]["code"]
        if code == 0:
            return True
        else:
            return False
    except:
        return False
    