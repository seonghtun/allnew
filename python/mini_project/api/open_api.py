import requests
import pandas as pd
import time
from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import json
import os.path

pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',50)

# pydantic.json.ENCODERS_BY_TYPE[objectid] = str

BASE_DIR = os.path.dirname(os.path.relpath("./"))
secret_file = os.path.join(BASE_DIR, "../../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    
    except KeyError:
        errorMsg = "Set the {} enviroment variable.".format(setting)
        return errorMsg

MONGO_HOST = get_secret('Mongo_Host')
JSON_HOST = get_secret('JSON_Host')

client = mongo_client.MongoClient(f'{MONGO_HOST}')

mydb = client['test']
mycol = mydb['netflix']

print('Connected to Mongodb.....')

def getAPI(url, country=None):
    if country is None:
        country = ''
        # 없이 검색하는거 다들고오는거
    else :
        country = '?country='+country
    response = requests.get(url + country)
    print(type(response.text))
    _dict = json.loads(response.text)
    return _dict

def mongo_insert(netflix_list):
    mycol.insert_many(netflix_list)
    result = mycol.find().limit(10)
    
    if result:
        return result
    else:
        return "검색 결과가 없습니다."

def mongo_delete():
    mycol.delete_many({})
    result = mycol.find()
    if len(list(result)) == 0 :
        return "empty collection"
    else:
        return result

datas = getAPI(JSON_HOST)
df = pd.DataFrame(datas)
print(df.loc[df['show_title']==('Squid Game'),['cumulative_weeks_in_top_10']])
print(df.loc[(df['show_title']==('Squid Game')) & (df['country_name'] == 'United States'),['country_name','cumulative_weeks_in_top_10']].groupby(['country_name']).max().sort_values(by=['cumulative_weeks_in_top_10'], axis=0, ascending=False))

# print(mongo_delete())
# print(list(mongo_insert(datas)))

# @app.get('/Mongoinsert')
# def mongoinsert():
#     result = MongoInsert(getAPI())
#     return result

# print(getAPI(url))