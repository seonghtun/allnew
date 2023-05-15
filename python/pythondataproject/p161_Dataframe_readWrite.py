import numpy as np
from pandas import Series, DataFrame

myindex = ['강호민', '유재준', '신동진']
mylist = [30, 40 ,50]

myseries = Series(data=mylist, index=myindex)
print('\nSeries print')
print(myseries)

myindex = ['강호민','유재준','이수진']
mycolumns = ['서울','부산','경주']
mylist = list(10 * onedata for onedata in range(1,10))

myframe = DataFrame(np.reshape(np.array(mylist), (3,3)),
                    index=myindex , columns=mycolumns)
print('\nDataFrame print')
print(myframe)

print('\nDataFrame + Series')
result = myframe.add(myseries, axis=0)
print(result)

myindex2 = ['강호민','유재준','김병준']
mycolumns2 = ['서울',' 부산', '대구']
mylist2 = list(5 * onedata for onedata in range(1,10))

myframe2 = DataFrame(np.reshape(np.array(mylist2), (3,3)),
                     index=myindex2, columns=mycolumns2)

print('\nDataFrame print')
print(myframe2)

print('\nDataFrame + DataFrame')
result = myframe.add(myframe2, fill_value = 0)
print(result)

myindex = ['이순신', '김유신','강감찬', '광해군','연산군']
mycolumns = ['서울','부산','광주','목포','경주']
mylist = list(10 * onedata for onedata in range(1,26))
print(mylist)

myframe = DataFrame(np.reshape(mylist, (5,5)), index=myindex,
                    columns=mycolumns)

print('\n1 row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result)

print('\nmulti row data read of series')
result = myframe.iloc[[1,3]]
print(type(result))
print(result)

print('\neven row data read of series')
result = myframe.iloc[0::2]
print(type(result))
print(result)

print('\nodd row data read of series')
result = myframe.iloc[1::2]
print(type(result))
print(result)

print('\n김유신 included row data read of series')
result = myframe.loc['김유신']
print(type(result))
print(result)

print('\n이순신, 강감찬 included row data read of Dataframe')
result = myframe.loc[['이순신', '강감찬']]
print(type(result))
print(result)

print(myframe.index)
print('-' * 50)

print('\n이순신, 광주 실적 included row data read of Dataframe')
result = myframe.loc[['이순신'],['광주']]
print(type(result))
print(result)

print('\n연산군, 강감찬 / 광주, 목포 실적 included row data read of Dataframe')
result = myframe.loc[['연산군','강감찬'], ['광주', '목포']]
print(type(result))
print(result)

print('\n이순신 ~ 강감찬 / 서울 ~ 목포 실적 included row data read of Dataframe')
result = myframe.loc['이순신':'강감찬', '서울':'목포']
print(type(result))
print(result)

print('\n김유신 ~ 광해군 / 부산 실적 included row data read of Dataframe')
result = myframe.loc['김유신' : '광해군', ['부산']]
print(type(result))
print(result)

print('\nBoolean Data process')
result = myframe.loc[[False, True, True, False, True]]
print(result)

print('\n부산 실적 <= 100')
result = myframe.loc[myframe['부산'] <= 100]
print(myframe['부산'] <= 100)
print(result)

cond1 = myframe['부산'] >= 70
cond2 = myframe['광주'] <= 140

print(type(cond1))
print('-' * 40)

df = DataFrame([cond1,cond2])
print(df)
print('-' * 40)

print(df.all())
print('-' * 40)

print(df.any())
print('-' * 40)

result = myframe.loc[df.all()]
print(result)
print('-' * 40)

result = myframe.loc[df.any()]
print(result)
print('-' * 40)

print('\nlambda function')
result = myframe.loc[lambda df : df['광주'] >= 80]
print(result)

print('\ndata set 30 => 이순신, 강감찬 부산 실적')
myframe.loc[['이순신','강감찬'],['부산']] = 30
print(myframe)

print('\ndata set 80 => 김유신 ~ 광해군 경주 실적')
myframe.loc['김유신':'광해군',['경주']] = 80
print(myframe)

print('\ndata set 50 => 연산군 모든 실적')
myframe.loc[['연산군'], :] = 50
print(myframe)

print('\ndata set 60 => 모든 사람의 광주 실적')
myframe.loc[:, ['광주']] = 60
print(myframe)

print('\ndata set 0 => 경주 실적 <= 60인 사람의 경주, 광주 실적')
myframe.loc[myframe['경주'] <= 60, ['경주', '광주']] = 0
print(myframe)