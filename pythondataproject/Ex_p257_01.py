import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10' \
      '_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg'
print(url)
filename = input("input the name about saving file.. ")

result = urllib.request.urlopen(url)
data = result.read()
print("# type(data) :",type(data))

f = open(filename, mode = 'wb')
f.write(data)
print(filename + ' Saved....')
f.close()