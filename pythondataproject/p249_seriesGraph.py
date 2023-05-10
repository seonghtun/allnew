import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame , Series
plt.rcParams['font.family'] = 'Malgun Gothic'

mylist = [30,20,40,30,60,50]
myindex = ['강감찬','김유신','이순신', '안익태', '윤동주', '홍길동']

print(myindex)
print(mylist)

myseries = Series(data=mylist, index=myindex)
myylim = [0, myseries.max() + 10]
myseries.plot(title='시험 점수', kind='line', ylim=myylim, grid=True, rot=10, use_index=True)

filename = 'seriesGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다.')
plt.show()