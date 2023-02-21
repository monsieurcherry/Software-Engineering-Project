import requests
#import dbinfo
import json
import time


api_key = 'a471198f1d4a279171da8f17892b64eb12c32f33'
contract_name = 'dublin'
api_query = 'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a471198f1d4a279171da8f17892b64eb12c32f33'
r = requests.get(api_query)
data = (json.loads(r.text))



def main():
    while True:
        try:
            r = requests.get(api_query)
            with open('json_data.json', 'w') as outfile:
                json.dump(data, outfile)
            time.sleep(5*60)
        except:
            print("Error. Something went wrong.")
    return 
main()