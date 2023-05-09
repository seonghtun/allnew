import pandas as pd

myframe = pd.read_csv('data02.csv', header=None, names=['이름','학년','국어','영어','수학'],index_col='이름')
print(myframe)