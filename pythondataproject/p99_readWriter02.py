myfile01 = open('sample02.txt', 'rt',encoding='UTF-8')
linelists = myfile01.readlines()
myfile01.close()

myfile02 = open('result02.txt', 'wt', encoding='UTF-8')
for line in linelists:
    mylist = line.strip().split(',')
    if int(mylist[1]) >= 19:
        myfile02.write(mylist[0] + '/'+ mylist[1] + '/' + '성인\n')
    else:
        myfile02.write(mylist[0] + '/' + mylist[1] + '/' + '미성년\n')
print("done~!!")
myfile02.close()

myfile03 = open('result02.txt', 'rt', encoding='UTF-8')
linelists = myfile03.readlines()
# print(linelists+'done')
for one in linelists:
    print(one)
myfile03.close()