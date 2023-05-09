import random
import pandas as pd
import sys
import os

dirname = './data'
# os.mkdir(dirname)

result = []
myColumns = ('번호', '이름', '나이')
myencoding = 'utf-8'

for idx in range(1,3):
    sublist = []
    sublist.append(100 * idx)
    sublist.append('김철수' + str(idx))
    sublist.append(random.randint(1,10))
    result.append(sublist)

myframe = pd.DataFrame(result, columns=myColumns)


filename = 'csv_01_01.csv'
filepath = os.path.join(dirname,filename)
myframe.to_csv(filepath, encoding=myencoding, mode='w', index=True)

filename = 'csv_01_02.csv'
filepath = os.path.join(dirname,filename)
myframe.to_csv(filepath, encoding=myencoding, mode='w', index=False)

filename = 'csv_01_03.csv'
filepath = os.path.join(dirname,filename)
myframe.to_csv(filepath, encoding=myencoding, mode='w', index=False , header=False)

filename = 'csv_01_04.csv'
filepath = os.path.join(dirname,filename)
myframe.to_csv(filepath, encoding=myencoding, mode='w', index=False , header=False)

