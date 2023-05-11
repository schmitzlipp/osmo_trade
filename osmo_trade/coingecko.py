import requests

def get_price(id: str, currency: str):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=osmosis&vs_currencies=usd"
    querystring = {"ids":id,"vs_currencies":currency, "include_last_updated_at":"true"}
    headers = {"Content-Type": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        response_dict = response.json()
        price = response_dict[id][currency]
        timestamp = response_dict[id]["last_updated_at"]
        return price, timestamp
    else:
        return None, None
    
            