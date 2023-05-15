import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'
mycolors=['blue','#6AFF00','yellow','#FF003C','green']
mylist = [30,20,40,60,50]
myindex = ['이상화','한용운','노천명','윤동주','이육사']

myseries = pd.Series(data=mylist, index=myindex)
myseries.plot(kind='pie',colors=mycolors, shadow=True, explode=(0,0.1,0,0,0), autopct='%1.2f%%',
             startangle=90, counterclock=False)
plt.legend(loc=4)
filename = 'ex_graph05.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename,'Saved....')
plt.show()
