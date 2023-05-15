from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'cheogajip'
base_url = 'https://www.cheogajip.co.kr/bbs/board.php'

def getData():
    saveData = []

    for page_idx in count():
        if page_idx >= 124:
            chknStore.save2Csv(saveData)
            break
        else:
            url = base_url
            url += '?bo_table=store'
            url += '&page=%s' % (str(page_idx + 1))

            chknStore = ChickenStore(brandName, url)
            soup = chknStore.getSoup()

            
            mytbody = soup.find('tbody')
            # print(mytbody)
            shopExists = False
            for mytr in mytbody.findAll('tr'):
                shopExists = True
                print("mytr.strings : ", mytr.strings)
                mylist = list(mytr.strings)
                print(mylist)

                store = mylist[1]
                address = mylist[3]
                phone = mylist[5]

                if len(address) >= 2:
                    imsi = address.split()
                    sido = imsi[0]
                    gungu = imsi[1]

                mydata = [brandName, store, sido, gungu, address,phone]
                print(mydata)
                saveData.append(mydata)
                
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')
