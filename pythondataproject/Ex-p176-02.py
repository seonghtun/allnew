from pandas import Series as sr

index = ['강감찬', '이순신', '김유신', '광해군','연산군','을지문덕']
mylist = [50,60,40,80,70,20]
myseries = sr(data= mylist, index=index)
print(myseries)

myseries[1] = 100
myseries[2:5] = 999
myseries[[0,-1]] = 30
print(myseries)