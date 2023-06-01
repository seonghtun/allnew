import requests
import pandas as pd
import time
from fastapi import FastAPI, Query
from pymongo import mongo_client
from bson.objectid import ObjectId
import json
import os.path
from datetime import datetime, timedelta
from dateutil import relativedelta
from pydantic import BaseModel
import pydantic
import gridfs
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine, text
from PIL import Image
import base64
from io import BytesIO
import io
from typing import List




# plt.rc('font', family='AppleGothic')

BASE_DIR = os.path.dirname(os.path.relpath("./"))
GRAPH_DIR = "../graph/"
secret_file = os.path.join(BASE_DIR, "../../secret.json")

pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',50)

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

class TotalGraph(BaseModel):
    title:str 
    countries:list = []

class PeriodGraph(BaseModel):
    title:str 
    countries:list = []
    period_start:str
    period_end:str

class Period(BaseModel):
    title:str
    period_start:str
    period_end:str

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
HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")
STORE_DIRECTORY = "/allnew/node/mini_project/public/result/"

user_list=["Squid Game", "All of Us Are Dead","Hometown Cha-Cha-Cha", "The Glory"]

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'
print(DB_URL)
engine = create_engine(DB_URL, pool_recycle=500)

client = mongo_client.MongoClient(f'{MONGO_HOST}')

mydb = client['test']
total_col = mydb['total_netflix']
period_col = mydb['period_netflix']

print('Connected to Mongodb.....')

def InsertImageDB(filenames):
## jpg dpi 100x100, png dpi 72x72
    for filename in filenames:
        with open("../graph/" + filename, "rb") as image_file:
            binary_image = image_file.read()
            binary_image = base64.b64encode(binary_image)
            binary_image = binary_image.decode('UTF-8')
            img_df = pd.DataFrame({'filename':filename,'graph_data':[binary_image]})
            result = img_df.to_sql('images', con=engine, if_exists='append', index=False)
            print(f'Image file : {filenames} Inserted~!!')
    # os.chdir('../')
    return None

def store_graph(q,STORE_DIRECTORY):
    with engine.connect() as conn:
        result = list(conn.execute(text(f"select * from images where filename='{q[0]}' or filename='{q[1]}'")))
    for i in range(len(result)):
        img = base64.b64decode(result[i].graph_data)
        im = Image.open(BytesIO(img))
        im.save(STORE_DIRECTORY + q[i])
    return True

def drop_table(table):
    with engine.connect() as conn:
        conn.execute('TRUnCATE TABLE users;')


def getAPI(countries=None,title=None,url = JSON_HOST, period=None):
    url += '?'
    if countries != None:
        for i in range(len(countries)):
            url += 'country=' + countries[i]+'&'
    if title==None:
        return print("제목은 들어와야 됩니다.")
    if period!=None:
        if len(period[0])==4:
            start = datetime.strptime(period[0],'%Y')
            end = datetime.strptime(period[1],'%Y')
        else:
            start = datetime.strptime(period[0],'%Y-%m')
            end = datetime.strptime(period[1],'%Y-%m')
        
        delta = relativedelta.relativedelta(end,start)
        for i in range(12 * delta.years + delta.months):
            date = start + relativedelta.relativedelta(months=i)
            url += f"week_like={date.year}-{date.month}&"
    url += 'show_title='+title
    response =  requests.get(url)
    if response.text == '[]':
        print("비어있어")
        return False
    _dict = json.loads(response.text)
    return _dict


@app.get(path='/netflix-total')
async def total(title):
    result = getAPI(title=user_list[int(title)])
    if not result:
        return {"ok": False, "data": []}

    total_col.insert_many(result)
    print(list(total_col.find().limit(10)))
    # 정렬된 top10 누적주수 제일 많은 나라 순 정렬해서

    df = pd.DataFrame(result)
    df = df.drop(columns="_id")
    df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype(int)

    order_dict = df.loc[df.groupby('country_name')['cumulative_weeks_in_top_10'].idxmax()]\
                        .sort_values(['cumulative_weeks_in_top_10'],ascending=False)\
                        .to_dict(orient='list')

    return {"ok": True, "data": order_dict}

@app.post(path='/netflix-month')
async def month(req:Period):
    result = getAPI(title=user_list[int(req.title)], period=[req.period_start,req.period_end])
    if not result:
        return {"ok": False, "data": []}
    period_col.insert_many(result)
    print(list(period_col.find({},{"_id":0}).limit(10)))

    # 정렬된 top10 누적주수 제일 많은 나라 순 정렬해서
    df = pd.DataFrame(result)
    df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype(int)

    order_dict = df.loc[df.groupby('country_name')['cumulative_weeks_in_top_10'].idxmax()]\
                        .sort_values(['cumulative_weeks_in_top_10'],ascending=False)\
                        .to_dict(orient='list')
    return {"ok": True, "data": order_dict}

@app.post(path='/netflix-year')
async def year(req:Period):

    result = getAPI(title=user_list[int(req.title)],period=[req.period_start,req.period_end])
    if not result:
        return {"ok": False, "data": []}
    period_col.insert_many(result)
    print(list(period_col.find().limit(10)))
    # 정렬된 top10 누적주수 제일 많은 나라 순 정렬해서

    df = pd.DataFrame(result)
    df['cumulative_weeks_in_top_10'] = df['cumulative_weeks_in_top_10'].astype(int)

    order_dict = df.loc[df.groupby('country_name')['cumulative_weeks_in_top_10'].idxmax()]\
                        .sort_values(['cumulative_weeks_in_top_10'],ascending=False)\
                        .to_dict(orient='list')
    
    return {"ok": True, "data": order_dict}

@app.get(path='/get_graph')
async def store_db_graph(q: List[str] = Query(None)):
    # STORE_DIRECTORY = "./result/"
    store_graph(q,STORE_DIRECTORY)
    return {"ok": True, "graph_urls" : q}

@app.post(path='/total-graph')
async def make_total_graph(req:TotalGraph):
    print(req.title, req.countries)
    filename1 = f"{'_'.join(req.countries).replace(' ','_')}.png"
    filename2 = f"{'_'.join(req.countries).replace(' ','_')}_1st.png"
    with engine.connect() as conn:
        result = list(conn.execute(text(f"select * from images where filename='{filename1}' or filename='{filename2}'")))

    if (len(result)==0):
        data = total_col.find({"$and":[{'country_name':{'$in':req.countries}},{"show_title":user_list[int(req.title)]}]},{"_id":0})
        data = list(data)
        if len(data) == 0:
            return {"ok": False, "graph_urls":[]}
        countries_rank_graph(data,req.countries,GRAPH_DIR + filename1,user_list[int(req.title)])
        data = total_col.find({'$and':[{'country_name':{'$in':req.countries}},{'weekly_rank':'1'},
        {"show_title":user_list[int(req.title)]}]},{"_id":0})
        data = list(data)
        if len(data) == 0:
            return {"ok": False, "graph_urls":[]}
        first_count_graph(data, GRAPH_DIR + filename2,user_list[int(req.title)]+ ' 1st')
        InsertImageDB([filename1, filename2])
    store_graph([filename1, filename2],STORE_DIRECTORY)
    return {"ok": True, "graph_urls": [filename1, filename2]}


@app.post(path='/month-graph')
async def make_month_graph(req:PeriodGraph):
    print(req.title, req.countries)
    filename1 = "_".join([req.period_start,req.period_start,req.title])+".png"
    filename2 = "_".join([req.period_start,req.period_start,req.title,"1st"])+".png"

    with engine.connect() as conn:
        result = list(conn.execute(text(f"select * from images where filename='{filename1}' or filename='{filename2}'")))

    if (len(result)==0):
        data = period_col.find({'$and':[{'country_name':{'$in':req.countries}},\
                                    {'show_title': user_list[int(req.title)]}]},{"_id":0})
        data = list(data)
        if len(data) == 0:
            return {"ok": False, "graph_urls":[]}
    
        countries_rank_period_graph(data,req.countries,GRAPH_DIR + filename1,user_list[int(req.title)],req.period_start,req.period_end)
        data = period_col.find({'$and':[{'country_name':{'$in':req.countries}},{'weekly_rank':'1'},\
                            {'show_title': user_list[int(req.title)]}]},{"_id":0})
        data = list(data)
        if len(data) == 0:
            return {"ok": False, "graph_urls":[]}
        first_count_graph(data, GRAPH_DIR + filename2,user_list[int(req.title)]+ ' 1st')
        InsertImageDB([filename1, filename2])
    store_graph([filename1, filename2],STORE_DIRECTORY)
    

    
    
    store_graph([filename1, filename2],STORE_DIRECTORY)
    return {"ok": True, "graph_urls":[filename1, filename2]}

@app.post(path='/year-graph')
async def make_year_graph(req:PeriodGraph):
    print(req.title, req.countries)

    data = period_col.find({'country_name':{'$in':req.countries}},{"_id":0})
    if len(list(data)) == 0:
        return {"ok": False, "graph_urls":[]}
    filename1 = 'YearGraph01.png'
    countries_rank_period_graph(data,req.countries,GRAPH_DIR + filename1,user_list[int(req.title)],req.period_start,req.period_end)
    
    data = period_col.find({'$and':[{'country_name':{'$in':req.countries}},{'weekly_rank':'1'},\
                        {'week':{'$gte': req.period_start, '$lt':req.period_end}}]},{"_id":0})
    
    filename2 = "YearGraph02.png"
    first_count_graph(data, GRAPH_DIR + filename2,user_list[int(req.title)] + ' 1st')

    
    return {"ok": True, "graph_urls":[filename1, filename2]}


@app.get(path='/col-drop')
async def drop(collection):
    if collection == 'total':
        print(total_col.find_one())
        total_col.delete_many({})
        print(total_col.find_one())
    else :
        print(period_col.find_one())
        period_col.delete_many({})
        print(period_col.find_one())
    return {"ok": True}

def date_range(start, end):
    if len(start) == 4:
        start = datetime.strptime(start,'%Y')
        # end = datetime.strptime(end,'%Y-%m') + relativedelta.relativedelta(months=1) - timedelta(days=1)
        end = datetime.strptime(end,'%Y') - timedelta(days=1)
    else :
        start = datetime.strptime(start,'%Y-%m')
        end = datetime.strptime(end,'%Y-%m') - timedelta(days=1)
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days + 1) ]
    return dates

def countries_rank_period_graph(data, countries,filename,title,start,end):
    df = pd.DataFrame(data)
    print(df.head())

    df['weekly_rank'] = df['weekly_rank'].astype(int)
    dates = date_range(start,end)
    print(dates[0],dates[-1])
    serieses = [pd.Series(index=dates,data=np.zeros_like(dates))]
    for country in countries:
        data = df.loc[df['country_name'] == country, ['week','weekly_rank']].set_index(['week'])
        data.columns = [country]
        serieses.append(data)
        
    graph_df = pd.concat(serieses,axis=1).sort_index().fillna(11)[countries]
    graph_df.plot(figsize=(10,6),title=title, legend=True,marker="o" ,linestyle='None', rot=15)
    
    for series in serieses[1:]:
        for i in range(len(series)):
            plt.text(dates.index(series.index[i]), series.values[i][0] -0.1, str(series.values[i][0]),
            horizontalalignment='center', color='red')
    
    plt.xlabel('date')
    plt.ylabel('Ranking')
    plt.yticks(range(1,11,1))
    plt.ylim(top=10)
    plt.gca().invert_yaxis()

    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + 'Saved...')
    plt.cla()
    return filename

def countries_rank_graph(data, countries,filename,title):
    df = pd.DataFrame(data)
    df['weekly_rank'] = df['weekly_rank'].astype(int)
    # print(df)
    serieses = []

    for country in countries:
        data = df.loc[df['country_name'] == country, ['week','weekly_rank']].set_index(['week'])
        data.columns = [country]
        serieses.append(data)
        # print(data.tail())

    graph_df = pd.concat(serieses,axis=1).sort_index().fillna(11)
    graph_df.plot(kind='line', figsize=(10,6),title=title, legend=True,marker="." , rot=15)
    for series in serieses:
         for i in range(len(series)):
            plt.text(list(graph_df.index).index(series.index[i]), series.values[i][0] - 0.2, str(series.values[i][0]),
            horizontalalignment='center', color='red')

    plt.xlabel('date')
    plt.ylabel('Ranking')
    plt.yticks(range(1,11,1))
    plt.ylim(top=10)
    plt.gca().invert_yaxis()

    plt.savefig(filename,dpi=400, bbox_inches='tight')
    print(filename + ' Saved...')
    plt.cla()
    return filename

def first_count_graph(data,filename,title):
    df = pd.DataFrame(data)
    print(df.head())
    place = df.groupby('country_name')['weekly_rank'].count()
    # 색깔 적용하는 코드 만들어야됨
    colors = ['r','g','b']

    place.plot(kind='bar', figsize=(10,6),title=title, rot=15, color=colors[:len(df.index)])
    
    plt.xlabel('Country')
    plt.ylabel('Count')
    
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + ' Saved...')
    plt.cla()
    return filename
# return 안해주면 해줄때 까지 