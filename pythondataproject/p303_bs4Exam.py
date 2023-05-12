from bs4 import BeautifulSoup

html = open("fruits.html", "r", encoding='utf-8')
soup = BeautifulSoup(html, "html.parser")
body = soup.select_one('body')
# print(type(body))
# ptags = soup.select('.ptag')
# print(ptags)
ptag = body.find('p')
print('1번째 p 태그 : ', ptag['class'])

ptag['class'][1] = 'white'

print('1번째 p 태그 : ', ptag['class'])

ptag['id'] = 'apple'
print('1번째 p 태그 id 속성 :', ptag['id'])

body_tag = soup.find('body')
print(body_tag)
print('-' * 50)

idx = 0
print('children 속성으로 하위 항목 보기')
print('white character 문자까지 포함')

for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 : ', child)

mydiv = soup.find('div')
print(mydiv)

print('div 태그 부모 태그는?')
print(mydiv.parent)
print('-' * 50)