import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

url = 'https://movie.daum.net/ranking/reservation'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html , 'html.parser')

infos = soup.findAll('div',attrs={'class':'thumb_cont'})
print(infos)

datas = []
for i,div in enumerate(infos):
    row = [i + 1,div.find('a',attrs={'class': 'link_txt'}).string,
           div.find('span',attrs={'class': 'txt_grade'}).string,
           div.find('span',attrs={'class': 'txt_num'}).string,
           div.find('span',attrs={'class': 'txt_info'})
           .find('span',attrs={'class': 'txt_num'}).string]
    print(row)
    datas.append(row)
columns = ['순위','제목','평점','예매율','개봉일']

df = DataFrame(data=datas, columns=columns)
print(df)