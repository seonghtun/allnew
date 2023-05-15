import pandas as pd

mydf01= pd.DataFrame({'name': ['김유신','김유신','이순신','박영효','이순신','이순신','김유신'],
                      'korean': [60,50,40,80,30,55,45]})
mydf02= pd.DataFrame({'name': ['이순신','김유신','신사임당'],
                      'english':[60,55,80]})

print(mydf01)
print('-' * 50)
print(mydf02)
print('-' * 50)


df_merge01 = pd.merge(mydf01, mydf02, on='name',indicator=True)
print('\n use on="name" merge dataframe ')
print(df_merge01)
print('-' * 50)

df_merge02 = pd.merge(mydf01, mydf02, on='name', how='outer',
                      suffixes=['','_'], indicator=True)
print('\n use on="name" how="outer" merge dataframe ')
print(df_merge02)
print('-' * 50)