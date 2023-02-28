import sqlalchemy as sqla
from sqlalchemy import create_engine
from pprint import pprint
import simplejson as json
import requests
from IPython.display import display

URI = "dbbikes.cfjfzkae45jy.eu-west-1.rds.amazonaws.com"
PORT="3306"
DB="dbbikes"
USER="admin"
PASSWORD = "mypassword"

engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)

sql = """
CREATE DATABASE IF NOT EXISTS dbbikes;
"""
engine.execute(sql)

def station_to_db(text):
    sql = """
    CREATE TABLE IF NOT EXISTS station (
    address VARCHAR(256),
    banking INTEGER,
    bike_stands INTEGER,
    bonus INTEGER,
    contract_name VARCHAR(256),
    name VARCHAR(256),
    number INTEGER,
    position_lat REAL,
    position_lng REAL,
    status VARCHAR(256)
    )
    """

    try:
        res = engine.execute("DROP TABLE IF EXISTS station")
        res
        res = engine.execute(sql)
        res
    except Exception as e:
        print(e)
    
    
    stations = json.loads(text)
    for station in stations:
        vals = (station.get('address'),
                int(station.get('banking')),
                station.get('bike_stands'),
                int(station.get('bonus')),
                station.get('contract_name'),
                station.get('name'),
                station.get('number'),
                station.get('position').get('lat'),
                station.get('position').get('lng'),
                station.get('status'))
        engine.execute("insert into station values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", vals)
    return




def availability_to_db(text):
    sql = """
    CREATE TABLE IF NOT EXISTS availability(
    number INTEGER,
    available_bikes INTEGER,
    available_bike_stands INTEGER,
    last_update INTEGER
    )
    """

    try:
        res = engine.execute("DROP TABLE IF EXISTS availability")
        res
        res = engine.execute(sql)
        res
    except Exception as e:
        print(e)
        
    stations = json.loads(text)
    for station in stations:
        vals = (int(station.get('number')),
                int(station.get('available_bikes')),
                int(station.get('available_bike_stands')),
                int(str(station.get('last_update')[0:11])))
        
        engine.execute("insert into availability values(%s,%s,%s,%s)", vals)
    return




api_key = 'a471198f1d4a279171da8f17892b64eb12c32f33'
contract_name = 'dublin'
api_query = 'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a471198f1d4a279171da8f17892b64eb12c32f33'

import time

def main():
    while True:
        try:
            r = requests.get(api_query)
            station_to_db(r.text)
            availability_to_db(r.text)
            print("scraping in progress")
            time.sleep(5*60) #Scrape every 5 minutes
        except:
            print("Error. Something went wrong.") 
    return

main()