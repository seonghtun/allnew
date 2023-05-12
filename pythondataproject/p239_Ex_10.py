import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'
myframe = pd.read_csv('mpg.csv')
print(myframe)
print(myframe.columns)
print(myframe['hwy'].max())
print(myframe['drv'].unique())

frame01 = myframe.loc[myframe['drv'] == 'f', 'hwy']
frame01.index.name = 'f'
print(frame01.head())
print('-' * 40)

frame02 = myframe.loc[myframe['drv'] == '4', 'hwy']
frame02.index.name = '4'
print(frame02.head())
print('-' * 40)

frame03 = myframe.loc[myframe['drv'] == 'r', 'hwy']
frame03.index.name = 'r'
print(frame03.head())
print('-' * 40)

total_frame = pd.concat([frame01,frame02,frame03], axis=1, ignore_index=True)
total_frame.columns = ['f', '4', 'r']
print(total_frame)
total_frame.plot(kind='box', title='고속도록 주행 마일수의 상자 수염')

plt.xlabel('구동 방식')
plt.ylabel('주행 마일수')

filename = 'ex_graph06.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()


