import csv
import json

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
json_data = {}

for i in range(len(csv_names)):
    with open(BASE_DIR + csv_names[i], 'rt', encoding='utf-8') as f:
        reader = csv.DictReader(f,delimiter='\t')
        json_data[keys[i]] = list(reader)

print(json_data[keys[0]][0],json_data[keys[1]][0],json_data[keys[2]][0],len(json_data))
with open(json_name, 'wt') as json_file:
    json.dump(json_data, json_file)