import requests
# import dbinfo
import json


api_key = 'a471198f1d4a279171da8f17892b64eb12c32f33'
contract_name = 'dublin'
api_query = 'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a471198f1d4a279171da8f17892b64eb12c32f33'
r = requests.get(api_query)
print(json.loads(r.content))

