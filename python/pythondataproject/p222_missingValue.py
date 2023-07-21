import numpy as np
import pandas as pd
from pandas import DataFrame, Series

filename = 'excel02.csv'

print('\n# 누락된 데이터가 있는 샘플 데이터프레임')
myframe = pd.read_csv(filename, index_col='이름')
print(myframe)


print('\n# fillna() 메소드를 이용한 다른 값 대체하기')
print(myframe.fillna(0, inplace=False))

print('\n# inplace=False이므로 원본은 변동사항이 없다.')
print(myframe)

print('\n# inplace=True 일땐 원본이 변환되고 return 값은 없다.')
# print(myframe.fillna(0, inplace=True))

print('\n# inplace=True이므로 원본이 변동되었다.')
print(myframe)


print('\n 누락된 데이터 샘플 데이터프레임')
myframe.loc[['강감찬','홍길동'],['국어','영어']] = np.nan
myframe.loc[['박영희','김철수'],['수학']] = np.nan
print(myframe)

print('\n 임의의 값을 다른 값으로 치환')
print('\n 국어,영어,수학 컬럼의 NaN 값들을 일괄 변경')

mydict = {'국어': 15, '영어': 25, '수학': 35}
print(myframe.fillna(mydict, inplace=True))
print('-' * 40)

myframe.loc[['박영희'],['국어']] = np.nan
myframe.loc[['홍길동'],['영어']] = np.nan
myframe.loc[['김철수'],['수학']] = np.nan

print(myframe)
print('-' * 40)
mydict = {
    '국어': myframe['국어'].mean() ,
    '영어': myframe['영어'].mean(),
    '수학': np.ceil(myframe['수학'].mean())}

print(myframe.fillna(mydict))
print('-' * 40)