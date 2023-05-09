from pandas import Series as sr, DataFrame as df


myseries = sr(data=[30,40,50], index=['윤봉길','김유신','신사임당'])
myframe = df(data={'용산구': [3,12,21], '마포구':[6,15,24], '서대문구':[9,18,27]}, index=['윤봉길','김유신','이순신'])
myframe2 = df(data={'용산구': [5,20,35], '마포구':[10,25,40], '은평구':[15,30,45]}, index=['윤봉길','김유신','이완용'])

print('\nDataFrame + Series')
print(myframe.add(myseries, axis=0))

print('\nDataFrame + DataFrame')
print(myframe.add(myframe2,fill_value=20))

print('\nDataFrame - DataFrame')
print(myframe.sub(myframe2, fill_value=10))

