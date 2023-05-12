import re

mylist = ['ab123','cd456','ef789','abc12']

regex = '[a-z]{2}\d{3}'
pattern = re.compile(regex)

print("# 문자 2개로 시작하고, 숫자 3개로 끝나는 항목")
totallist = []
for item in mylist:
    if pattern.match(item):
        print(item, '은(는) 조건에 적합')
        totallist.append(item)

    else:
        print(item, "은(는) 조건에 부적합")

print('적합한 항목들')
print(totallist)