import pandas as pd
import numpy as np
from pandas import DataFrame, Series

before = DataFrame(data={'국어':[60,np.nan, 40],'영어':[np.nan,80,50],'수학':[90,50,np.nan]},
                   index=['강감찬','김유신','이순신'])
print('\n# Before')
print(before)

after = before.copy()

after.loc[before['국어'].isnull(),['국어']] = before['국어'].mean()
after.loc[before['영어'].isnull(),['영어']] = before['영어'].mean()
after.loc[before['수학'].isnull(),['수학']] = before['수학'].mean()

print("\n# After")
print(after)
print('-' * 40)
print(after.describe())
# mydict = {'국어': before['국어'].mean(),
#           '영어' : before['영어'].mean(),
#           '수학' : before['수학'].mean()}
#
# after = before.fillna(mydict)
# print(after)