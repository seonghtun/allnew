import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

plt.rcParams['font.family'] = 'Malgun Gothic'

mylist= [30, 20, 40, 60, 50]
myindex = ['이상화', '한용운','노천명','윤동주','이육사']

myseries = Series(data=mylist, index=myindex)
myylim=[0,myseries.max() + 10]
myseries.plot(title='금월 실적', kind='line', ylim=myylim, grid=False, rot=10, use_index=True)

filename = 'seriesGraph02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename, '파일이 저장되었습니다.')
plt.show()