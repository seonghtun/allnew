import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

myframe = pd.read_csv('tips.csv',index_col='Unnamed: 0')

print(myframe)

plt.rcParams['font.family'] = 'Malgun Gothic'
mycolors = ['r','g']
labels = ['Female','Male']
cnt = 0
for finditem in labels:
    xdata = myframe.loc[myframe['sex'] == finditem, 'total_bill']
    ydata = myframe.loc[myframe['sex'] == finditem, 'tip']

    plt.plot(xdata, ydata, color=mycolors[cnt], linestyle='None',marker='o', label=finditem)
    cnt+=1


plt.legend(loc=4)
plt.xlabel('결재 총액')
plt.ylabel('팁 비용')
plt.title('결재 총액과 팁 비용의 산점도')
plt.grid(True)

plt.show()