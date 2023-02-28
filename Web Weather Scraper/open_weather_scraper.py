import requests
import json

api_key = 'b7d6a55bc0fff59fb0d5f7c3c1668417'
lat='53.35'
lon='-6.26'
city = 'dublin'
api_query = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"


r = requests.get(api_query)
print(json.loads(r.text))