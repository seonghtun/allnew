import pandas as pd

atable = pd.read_csv('data03.csv', encoding='utf-8')
btable = pd.read_csv('data04.csv', encoding='utf-8', header=None)

print(atable)
print('-' * 50)
print(btable)
print('-' * 50)
btable.columns = atable.columns
result = pd.concat(objs=[atable,btable],ignore_index=True,axis=0)

filename = 'ex_p352_01_result.csv'
result.to_csv(filename, index=False,encoding='utf-8')
print(filename+' saved....')
print(result)