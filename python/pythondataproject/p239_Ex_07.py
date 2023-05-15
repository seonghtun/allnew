import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd

mydf = pd.read_csv('mygraph.csv', index_col='이름')
print(mydf)
mydf.index.name = '이름'
mydf.columns.name = '시험 과목'
plt.rcParams['font.family'] = 'Malgun Gothic'

mydf.plot(kind='bar', grid=False, table=False, stacked=True, rot=0,
          title='학생별 누적 시험 점수', legend=True, color=['C0','C1'])


plt.savefig('ex_graph04.png', dpi=400, bbox_inches='tight')
plt.show()