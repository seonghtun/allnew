import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

plt.rcParams['font.family'] = 'Malgun Gothic'
mylist = [30, 20 , 40 ,30, 60]
myindex = ['강감찬', '김유신','이순신','안익태', '윤동주']

myseries = Series(data=mylist, index=myindex)

myseries.plot(kind='bar', title='학생별 시험 점수',use_index=True,rot=0,
              table=False,grid=False, color=['r','g','b','y','m'])

plt.xlabel('학생 이름')
plt.ylabel('점수')

meanvalue=myseries.mean()
average = '평균 : %d건' % meanvalue
plt.axhline(y=meanvalue, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0,y=meanvalue + 1, s=average, horizontalalignment='center')

ratio = 100 * myseries / myseries.sum()
print("\n# ratio 구하기")
print(ratio)
for idx in range(myseries.size):
    value = str(myseries[idx]) + '건'
    ratioval = '%.1f%%' % ratio[idx]
    plt.text(x=idx,y=myseries[idx]/2, s=ratioval,
             horizontalalignment='center')
    plt.text(x=idx, y= myseries[idx]+1, s=value,
             horizontalalignment='center')
plt.savefig('graph02.png')
print('graph02.png Saved....')
plt.show()