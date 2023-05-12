from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

html = open('ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, "html.parser")
# body = soup.select_one('body')
#
# tbody = body.find('tbody')
# tbody_trs = tbody.findAll('tr')
# names = []
# datas = {}
# for tr in tbody_trs:
#     names.append(tr.find('td').text)
#
# print(names)
#
#
# for tr in tbody_trs:
#     datas[tr.find('td')]

result = []
columns = []
tbody = soup.find('tbody')
thead = soup.find('thead')
ths = thead.findAll('th')
tds = tbody.findAll('td')


for column in ths:
    columns.append(column.text)

for data in tds:
    result.append(data.text)

print(result)

nd_result = np.array(result).reshape((4,3))
print(nd_result)

print(columns)

df = pd.DataFrame(data=nd_result,columns = columns)
myframe = df.set_index(['이름'])
myframe = myframe.astype(float)
# myframe['HTML'] = myframe['HTML'].astype('int64')
# myframe['CSS'] = myframe['CSS'].astype('int64')
print(myframe)



myframe.plot(kind='line',legend=True,title='Exam', rot = 10)
plt.xlabel('이름')
plt.ylabel('성적')

plt.savefig('Ex06.png', dpi=400, bbox_inches='tight')
print('Ex06.png Saved....')
plt.show()
