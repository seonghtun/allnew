from pandas import Series as sr

index = ['성춘향', '이몽룡', '심봉사']
mylist = [40,50,60]

myseries = sr(data=mylist, index=index)

index2 = ['성춘향', '이몽룡', '뺑덕어멈']
mylist2 = [20,40,70]

myseries2 = sr(data=mylist2, index=index2)

myseries3 = myseries.add(myseries2, fill_value=10)

myseires4 = myseries.sub(myseries2, fill_value=30)

print(myseries3)
print(myseires4)

