from pandas import Series as sr

index = ['손오공', '저팔계', '사오정', '삼장법사']
mylist = [200,300,400,100]
myseries = sr(data= mylist, index=index)

myseries.index.name = '실적현황'
myseries.name = '직원 실적'

print('\n# 시리즈의 색인 이름')
print(myseries.index.name)

print('\n# 시리즈의 이름')
print(myseries.name)

print('\n# 반복하여 출력해보기')
for idx in myseries.index:
    print(f'색인 : {idx:>4s}, 값 : {myseries[idx]}')