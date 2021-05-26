import requests

headers = {'Accepts': 'application/json',
           'X-CMC_PRO_API_KEY':  '250f64bb-56e4-4a33-8831-6abacfd85df9'}


data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                    headers=headers).json()


lista = {}
for moneda in data['data']:
    a = moneda["symbol"]
    b = moneda["name"]
    lista[a] = b

print(lista)
