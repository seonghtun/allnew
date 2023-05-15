import pandas as pd
import numpy as np

from pandas import DataFrame, Series

print('\n# 시리즈의 누락된 데이터 처리하기')
print('# 원본 시리즈')
myseries = Series(['강감찬','이순신',None,np.nan, '광해군'])
print(myseries)

print('\n# isnull() 함수는 값이 NaN이면 True를 반환합니다.')
print('# 파이썬의 None도 NaN으로 취급됩니다.')
print(myseries.isnull())
print(myseries[myseries.isnull()])

print('\n# notnull() 인자를 이용하여 참인 항목들만 출력합니다.')
print(myseries[myseries.notnull()])
print('-' * 40)

print('\n# dropna() 함수는 누락된 데이터가 있는 행과 열을 제외시킨다.')
print(myseries.dropna())



filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')

print('\n# dropna() 이용 누락 데이터 처리')
cleaned = myframe.dropna()
print(cleaned)

print('\n# how="all" 이용 누락 데이터 처리')
cleaned = myframe.dropna(how='all', axis = 0)
print(cleaned)

print('\n# how="any" 이용 누락 데이터 처리')
cleaned = myframe.dropna(how='any', axis=0)
print(cleaned)

print('\n# [영어] 칼럼에 Nan 제거')
cleaned = myframe.dropna(subset=['영어'])
print(cleaned)

print('\n# 칼럼 기준, how="any" 이용 누락 데이터 제거')
cleaned = myframe.dropna(axis=1, how='any')
print(cleaned)

print(myframe)
myframe.loc[['강감찬','홍길동'],['국어']] = np.nan
print(myframe)

print('\n# 칼럼 기준, how="all" 이용 누락 데이터 제거')
cleaned = myframe.dropna(axis=1, how='all')
print(cleaned)

print('\n# thresh(1) 이용 누락 데이터 제거')
cleaned = myframe.dropna(axis=1, thresh=2)
print(cleaned)
