import sqlalchemy as sqla
from sqlalchemy import create_engine
from pprint import pprint
import simplejson as json
import requests
from IPython.display import display
import datetime
import time


engine = create_engine

URI = "dbbikes.cfjfzkae45jy.eu-west-1.rds.amazonaws.com"
PORT="3306"
DB="dbbikes"
USER="admin"
PASSWORD = "mypassword"

engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)

connection = engine.connect()

# connection.execute("DROP TABLE IF EXISTS combined;")

connection.close()

