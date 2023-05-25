import requests
import pandas as pd
import time
from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import json
import os.path
from datetime import datetime, timedelta

pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',50)

# pydantic.json.ENCODERS_BY_TYPE[objectid] = str

app = FastAPI()

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

def getAPI(country=None, show_title=None, category=None, week=None, url = JSON_HOST):
    url += '?'
    if country is not None:
        url += 'country='+country
    if show_title is not None:
        if url[-1] != "?":
            url += '&show_title='+show_title
        else :
            url += 'show_title='+show_title
    if category is not None:
        if url[-1] != "?":
            url += '&category='+category
        else :
            url += 'category='+category
    if week is not None:
        if url[-1] != "?":
            url += '&week='+week
        else :
            url += 'week='+week
    response = requests.get(url)
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

@app.get('/')
async def hello():
    return 'Hello yoon'

@app.get(path='/getdata')
async def json_server_get(country = None, title = None, category = None, date=None):
    print(country, title,category)
    if (category == 0):
        category = 'Films'
    else:
        category = 'TV'
    result = getAPI(country=country, show_title=title, category=category, date=date)
    return result


# df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype('int')

# print(df.info())

# def title_top10_country(show_title):
#     return df.loc[df['show_title']==(show_title),['country_name','show_title', 'cumulative_weeks_in_top_10' ]].\
#     groupby(['country_name']).max().sort_values('cumulative_weeks_in_top_10',ascending=False).head(10)

# # print(pd.to_datetime(df['week']).dt.month == 5)

# def weeks_top10(df,show_titles, countries):
#     pass
#     # show country weeks
#     list()
#     []

# print(df.loc[(df['show_title'] == 'Squid Game') & (df['country_name'] == 'Argentina')])

# squid_game_countries = title_top10_country('Squid Game')
# home_town_countries = title_top10_country('Hometown Cha-Cha-Cha')
# the_glory_countries = title_top10_country('The Glory')
# all_of_us_are_dead_countries = title_top10_country('All of Us Are Dead')

# merge titles
# print(squid_game_countries)
# print(home_town_countries)
# print(the_glory_countries)
# print(all_of_us_are_dead_countries)

# squid_home_merge = pd.merge(squid_game_countries, home_town_countries,suffixes=('_squid','_home_town') ,left_index=True, right_index=True,how='outer')
# print(squid_home_merge)
# glory_dead_merge = pd.merge(the_glory_countries, all_of_us_are_dead_countries,suffixes=('_glory','_dead') ,left_index=True, right_index=True,how='outer')
# print(glory_dead_merge)

# four_title_merge = squid_home_merge.join(glory_dead_merge, how='outer')
# print(four_title_merge.shape)
# print(four_title_merge.dropna(thresh=6, axis=0))
# print(four_title_merge.dropna(thresh=4, axis=0))






# print(mongo_delete())
# print(list(mongo_insert(datas)))

# @app.get('/Mongoinsert')
# def mongoinsert():
#     result = MongoInsert(getAPI())
#     return result

# print(getAPI(url))