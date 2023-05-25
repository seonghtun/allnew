import csv
import json
import pandas as pd
# pd.set_option('display.max_columns', 10)

# filename = './data/all-weeks-countries.tsv'
# df = pd.read_csv(filename, sep='\t')
# print(df)
# print(df[df['show_title'] == 'Squid Game'])
# print(df.columns)

# df.to_json('/allnew/node/jsonserver/netflix.json', orient='records')
BASE_DIR = 'data/'
csv_names = ['all-weeks-countries.tsv' ,'all-weeks-global.tsv', 'most-popular.tsv']
json_name = '/allnew/node/jsonserver/netflix.json'
keys = ['countries','global','most-popular']

def tsv_to_json(csv_names,json_name,keys):
    json_data = {}

    for i in range(len(csv_names)):
        with open(BASE_DIR + csv_names[i], 'rt', encoding='utf-8') as f:
            reader = csv.DictReader(f,delimiter='\t')
            json_data[keys[i]] = list(reader)
        print(json_data[keys[i]][0])

    with open(json_name, 'wt') as json_file:
        json.dump(json_data, json_file)
    return json_data

xls_names = ['국적별 입국_months.xls' ,'국적별 입국_years.xls']
json_name = '/allnew/node/jsonserver/tourist.json'
keys = ['months','years']
json_data = {}

for i in range(len(xls_names)):
    json_data[keys[i]] = pd.read_excel(BASE_DIR + xls_names[i]).drop(index=0).to_dict(orient='records')
    print(json_data[keys[i]][0])

with open(json_name, 'wt') as json_file:
    json.dump(json_data, json_file)


