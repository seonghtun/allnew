import pandas as pd

seoul = pd.read_csv('seoul.csv')
# print(seoul.head())
print(seoul[seoul['시군구'] == ' 서울특별시 강남구 신사동'])

result = seoul.loc[(seoul['시군구'] == ' 서울특별시 강남구 신사동') & (seoul['단지명'] == '삼지')]
print(result)

newdf = seoul.set_index(keys=['도로명'])
print(newdf[newdf.index == '언주로'])
print(newdf.loc[['동일로']].shape) # index 검색을 loc으로 할수있다. 원래 index 검색이었구나.
