import os.path
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import re
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.relpath("./"))
secret_file = os.path.join(BASE_DIR,'../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

YOUTUBE_KEY = get_secret('Youtube_apiKey')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey=YOUTUBE_KEY)
search_response = youtube.search().list(
    q='넷플릭스 한국 콘텐츠 해외 반응',
    order = 'relevance',
    part = 'snippet',
    maxResults = 50
).execute()

print(search_response['items'][0]['snippet']['title'])
print(search_response['items'][0]['id']['videoId'])

video_ids = []
video_titles = []

for item in search_response['items']:
    video_titles.append(item['snippet']['title'])
    video_ids.append(item['id']['videoId'])

print(len(video_titles), len(video_ids))

video_df = pd.DataFrame()
video_df['video_title'] = video_titles
video_df['video_id'] = video_ids

titles =[]
ids = []
dates = []
views = []
likes = []
favorits = []
comments = []
hours = []
mins = []
secs = []
tags = []

for i in range(len(video_df)):
    request = youtube.videos().list(
        id = video_df['video_id'][i],
        part = 'snippet,contentDetails,statistics'
    )

    response = request.execute()

    print(response)
    if response['items'] == []:
        continue
    
    else:
        titles.append(response['items'][0]['snippet']['title'])
        ids.append(response['items'][0]['id'])
        dates.append(response['items'][0]['snippet']['publishedAt'].split('T')[0])
        if response['items'][0]['snippet'].get('tags', False) == False:
            tags.append(np.NaN)
        else :
            tags.append(response['items'][0]['snippet']['tags'])
        views.append(response['items'][0]['statistics']['viewCount'])
        likes.append(response['items'][0]['statistics']['likeCount'])
        favorits.append(response['items'][0]['statistics']['favoriteCount'])
        if response['items'][0]['statistics'].get('commentCount', False) == False:
            comments.append(np.NaN)
        else :
            comments.append(response['items'][0]['statistics']['commentCount'])       
        duration = re.findall(r'\d+', response['items'][0]['contentDetails']['duration'])
        if len(duration) == 3:
            hours.append(duration[0])
            mins.append(duration[1])
            secs.append(duration[2])
        elif len(duration) == 2:
            hours.append(np.NaN)
            mins.append(duration[0])
            secs.append(duration[1])
        else:
            hours.append(np.NaN)
            mins.append(np.NaN)
            secs.append(duration[0])

detail_df = pd.DataFrame([titles,ids,dates,views,likes,favorits,comments,tags,hours,mins,secs]).T
# print(detail_df)
detail_df.columns = ['title','id','date','view','like','favorit','comment','tags','hour','min','sec']

print(detail_df)