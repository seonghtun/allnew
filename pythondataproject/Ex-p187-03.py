import pandas as pd

myColumns = ('이름','나이')
myencoding = 'utf-8'
mydata = [('김철수', 10), ('박영희', 20)]

myframe = pd.DataFrame(data=mydata, columns=myColumns)
print(myframe)
myframe2 = pd.DataFrame(data=mydata, columns=myColumns)
print(myframe2)

myframe.to_csv('csv_02_01.csv', index=False)
myframe2.to_csv('csv_02_02.csv', index=False, sep='#')

myframe = pd.read_csv('csv_02_01.csv')
print(myframe)

myframe2 = pd.read_csv('csv_02_02.csv')
print(myframe2)