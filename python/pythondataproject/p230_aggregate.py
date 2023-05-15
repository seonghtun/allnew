import numpy as np
from pandas import DataFrame

mydata = [[10.0, np.nan, 20.0],[20.0,30.0,40.0],\
          [np.nan,np.nan,np.nan],[40.0, 50.0, 30.0]]

myindex = ['이순신', '김유신','윤봉길', '계백']
mycolumn=['국어','영어','수학']
myframe=DataFrame(data=mydata,
                  index=myindex, columns=mycolumn)

print('\n# 성적 데이터프레임 출력')
print(myframe)

print('\n# 집계 함수는 기본값으로 누락된 데이터(NaN)를 배제하고 연산합니다.')
print('\n# sum 함수 사용 시 (axis=0)은 열 방향으로 합산합니다.')
print(myframe.sum(axis=0))

print('\n# sum 함수 사용 시 (axis=1)은 행 방향으로 합산합니다.')
print(myframe.sum(axis=1))

print('\n# mean, axis=1, skipna=False 옵션 사용하기')
print(myframe.mean(axis=1, skipna=False))

print('\n# mean, axis=0, skipna=False 옵션 사용하기')
print(myframe.mean(axis=0, skipna=False))

print('\n# mean, axis=1, skipna=True 옵션 사용하기')
print(myframe.mean(axis=0, skipna=True))

print('\n# max, axis=0, skipna=False 옵션 사용하기')
print(myframe.max(axis=0, skipna=False))

print('\n# max, axis=0, skipna=True 옵션 사용하기')
print(myframe.max(axis=0, skipna=True))


print(myframe)
print('\n# idxmax 최대값을 가진 색인 출력')
print(myframe.idxmax(axis=1,skipna=True))

print('\n# 누적합 메소드, axis=0 출력')
print(myframe.cumsum(axis=0))

print('\n# 누적합 메소드, axis=1 출력')
print(myframe.cumsum(axis=1))

print(myframe)

print('\n# 최대 요소 메소드, axis=1 출력')
print(myframe.cummax(axis=1))

print('\n# 최소 요소 메소드, axis=1 출력')
print(myframe.cummin(axis=1))


myframe.loc[myframe['국어'].isnull(), '국어'] = myframe['국어'].min() - 5
myframe.loc[myframe['영어'].isnull(), '영어'] = myframe['영어'].min() - 5
myframe.loc[myframe['수학'].isnull(), '수학'] = myframe['수학'].min() - 5

print(myframe)

print(myframe.describe())