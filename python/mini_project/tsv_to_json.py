import csv
import json

# pd.set_option('display.max_columns', 10)

# filename = './data/all-weeks-countries.tsv'
# df = pd.read_csv(filename, sep='\t')
# print(df)
# print(df[df['show_title'] == 'Squid Game'])
# print(df.columns)

# df.to_json('/allnew/node/jsonserver/netflix.json', orient='records')

csv_name = 'data/all-weeks-countries.tsv'
json_name = '/allnew/node/jsonserver/netflix.json'


with open(csv_name, 'rt', encoding='utf-8') as f:
    reader = csv.DictReader(f,delimiter='\t')
    json_data = {"datas" : list(reader)}

with open(json_name, 'wt') as json_file:
    json.dump(json_data, json_file)