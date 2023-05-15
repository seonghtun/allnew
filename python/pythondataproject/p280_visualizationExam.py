import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

font_location = 'c:/windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(
    fname=font_location
).get_name()

matplotlib.rc('font', family=font_name)

theaterfile = 'theater.csv'
colnames = ['id', 'theater', 'region', 'bindo']
dftheater = pd.read_csv(theaterfile, names=colnames, header=None)
dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater','region','bindo'])
dftheater.index.name = 'id'
print('전체조회')
print(dftheater)
print('-'*40)

print('극장별 상영 횟수 집계')
print('시리즈 이용 데이터프레임 생성')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

# print(sumSeries)
print('Series 3개를 이용하여 DataFrame 만들기')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis=1)
df.columns = ['합계', '평균', '개수']
print(df)

df.plot(kind='barh', rot=0)

# pandas len 은 row에 길이 개수가 된다. 데이터 개수지 그러면
plt.title(str(len(df)) + '개 매장 집계 데이터')
filename = 'visualizationExam_01.png'

plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
print(filename + ' Saved...')

print('집계 메소드를 사전에 담아 전달하기')
print('지역의 개수와 상영 회수의 총합')
mydict = {'bindo' : 'sum', 'region':'size'}
result = dftheater.groupby('theater').agg(mydict)
print(result)
print('-' * 50)

print('넘파이를 이용한 출력')
result = mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-' * 50)

def myroot(values):
    mysum = sum(values)
    return sqrt(mysum)

def plus_add(values, somevalue):

    result = myroot(values)
    return result + somevalue

mygrouping = dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용하기')
result = mygrouping.agg(myroot)
print(result)
print('-' * 30)

print('groupby와 사용자 정의 함수 (매개변수 2개) 사용하기')
result = mygrouping.agg(plus_add, somevalue=3)
print(result)

print('컬럼 2개 이상을 그룹핑하기')
newgrouping = dftheater.groupby(['theater', 'region'])['bindo']
result = newgrouping.count()
print(result)
print('-' * 30)

newDf = df.loc[:,['평균','개수']]
newDf.plot(kind='bar', rot=0)
plt.title('3개 극장의 평균과 상영관 수 ')

filename = 'visualizationExam_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
plt.show()

# labels : 원주 외곽에 보여줄 라벨
labels = []
explode = (0, 0.03, 0.06)

for key in sumSeries.index:
    mydata = key + '(' + str(sumSeries[key]) + ')'
    labels.append(mydata)

fig1, ax1 = plt.subplots()
mytuple = tuple(labels)
ax1.pie(sumSeries, explode=explode, labels=mytuple, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()
ax1.axis('equal')
filename ='visualizationExam_03.png'
plt.savefig(filename, dpi=400 , bbox_inches='tight')
print(filename,'Saved...')
