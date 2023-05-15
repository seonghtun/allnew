import pandas as pd

pelicana = pd.read_csv('pelicana.csv',encoding='utf-8')
cheogajip = pd.read_csv('cheogajip.csv',encoding='utf-8')

result = pd.concat(objs=[pelicana, cheogajip], axis=0, ignore_index=True)

print(result)