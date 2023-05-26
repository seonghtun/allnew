import requests
import pandas as pd
import time
from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import json
import os.path
from datetime import datetime, timedelta
from pydantic import BaseModel
import pydantic
import bson
from bson.objectid import ObjectId
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.relpath("./"))
GRAPH_DIR = "../graph/"
secret_file = os.path.join(BASE_DIR, "../../secret.json")

pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',50)

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

class GraphElements(BaseModel):
    title:str 
    countries:list = []

class Netflix(BaseModel):
    title: str
    period_start: str
    period_end: str
    

app = FastAPI()



with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    
    except KeyError:
        errorMsg = "Set the {} enviroment variable.".format(setting)
        return errorMsg

MONGO_HOST = get_secret('Mongo_Host')
JSON_HOST = get_secret('Netflix_JSON_Host')

user_list=["Squid Game", "All of Us Are Dead","Hometown Cha-Cha-Cha", "The Glory"]

client = mongo_client.MongoClient(f'{MONGO_HOST}')

mydb = client['test']
total_col = mydb['total_netflix']
period_col = mydb['period_netflix']
graph_col = mydb['graphs']


print('Connected to Mongodb.....')


def getAPI(countries=None,title=None,url = JSON_HOST, period=None):
    url += '?'
    if countries != None:
        for i in range(len(countries)):
            url += 'country=' + countries[i]+'&'
    if title==None:
        return print("제목은 들어와야 됩니다.")
    if period!=None:
        url += f"week_gte={period[0]}&week_lte={period[1]}&"
    url += 'show_title='+title
    response =  requests.get(url)
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

@app.get(path='/netflix_total_country')
async def country(title):
    result = getAPI(title=user_list[int(title)])
    if len(result) == 0:
        return "데이터가 없습니다."
    total_col.insert_many(result)
    # 정렬된 top10 누적주수 제일 많은 나라 순 정렬해서

    df = pd.DataFrame(result)
    df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype(int)

    order_dict = df.loc[df.groupby('country_name')['cumulative_weeks_in_top_10'].idxmax()]\
                        .sort_values(['cumulative_weeks_in_top_10'],ascending=False)\
                        .to_dict(orient='records')
    print(type(order_dict))
    return order_dict

@app.post(path='/netflix_period_country')
async def netflix_period(request:Netflix):
    print(request.period_start)
    start = datetime.strptime(request.period_start,"%Y-%m").date()
    end = datetime.strptime(request.period_end,"%Y-%m").date()
    result = getAPI(title=user_list[int(request.title)], period=[start,end])

    # 정렬된 top10 누적주수 제일 많은 나라 순 정렬해서
    df = pd.DataFrame(result)
    df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype(int)

    order_dict = df.loc[df.groupby('country_name')['cumulative_weeks_in_top_10'].idxmax()]\
                        .sort_values(['cumulative_weeks_in_top_10'],ascending=False)\
                        .to_dict(orient='records')
    return order_dict

@app.post(path='/total_graph')
async def make_graph(req : GraphElements):
    print(req.title, req.countries)
    graphs = []
    data = total_col.find({'country_name':{'$in':req.countries}},{"_id":0})
    filename = 'Graph01.png'
    
    countries_rank_graph(data,req.countries,GRAPH_DIR + filename,user_list[int(req.title)])
    with open(GRAPH_DIR + filename, 'rb') as f:
        graphs.append({"filename":filename, "imagefile" : f.read()})    
    
    data = total_col.find({'$and':[{'country_name':{'$in':req.countries}},{'weekly_rank':'1'}]},{"_id":0})
    filename = "Graph02.png"
    first_count_graph(data, GRAPH_DIR + filename,user_list[int(req.title)]+ ' 1st')
    with open(GRAPH_DIR + filename, 'rb') as f:
        graphs.append({"filename":filename, "imagefile" : f.read()})   
    
    graph_col.insert_Many(bson.BSON.encode(graphs))
    return filename

def countries_rank_graph(data, countries,filename,title):
    df = pd.DataFrame(data)
    df['weekly_rank'] = df['weekly_rank'].astype(int)
    
    serieses = []
    
    for country in countries:
        data = df.loc[df['country_name'] == country, ['week','weekly_rank']].set_index(['week'])
        data.columns = [country]
        serieses.append(data)
        # print(data.tail())
    
    graph_df = pd.concat(serieses,axis=1).sort_index().fillna(11)
    graph_df.plot(kind='line', figsize=(10,6),title=title, legend=True,marker="." , rot=15)
    
    plt.xlabel('date')
    plt.ylabel('Ranking')
    plt.yticks(range(1,11,1))
    plt.ylim(top=10)
    plt.gca().invert_yaxis()

    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + 'Saved...')
    plt.cla()
    return filename

def first_count_graph(data,filename,title):
    df = pd.DataFrame(data)
    place = df.groupby('country_name')['weekly_rank'].count()
    # 색깔 적용하는 코드 만들어야됨
    colors = ['r','g','b']

    place.plot(kind='bar', figsize=(10,6),title=title, rot=15, color=colors)
    
    plt.xlabel('Country')
    plt.ylabel('Count')
    
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + 'Saved...')
    plt.cla()
    return
# return 안해주면 해줄때 까지 

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