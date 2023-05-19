import json, urllib.request, datetime, math, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
##abspath가 절대경로
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets= json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return print(errorMsg)



def getRequestUrl(url):
    req = urllib.request.Request(url)
    try : 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getHospitalData(pageNo, numofRows):
    endpoint = 'http://apis.data.go.kr/6260000/MedicInstitService/MedicalInstitInfo'
    
    parameters = ''
    parameters += '?resultType=json'
    parameters += '&serviceKey='+get_secret('data_apiKey')
    parameters += '&numOfRows=' + str(numofRows)
    parameters += '&pageNo=' + str(pageNo)
    url = endpoint + parameters

    print('URL')
    print(url)

    result = getRequestUrl(url)
    print(result)
    if(result == None):
        return None
    else:
        return json.loads(result)

jsonResult = []

pageNo = 1
numofRows = 100
nPage = 0


while (True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))
    jsonData = getHospitalData(pageNo, numofRows)
    print(jsonData)

    if (jsonData['MedicalInstitInfo']['header']['resultCode'] == '00'):
        totalCount = jsonData['MedicalInstitInfo']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)

        for item in jsonData['MedicalInstitInfo']['body']['items']['item']:
            jsonResult.append(item)
        
        if totalCount == 0:
            break
        nPage = math.ceil(totalCount / numofRows)
        if (pageNo == nPage):
            break
        pageNo += 1
    else:
        break

saveFilename = 'xx_Busan_medical.json'
with open(saveFilename, 'w', encoding='utf-8') as outfile:
    retJson = json.dumps(jsonResult, indent=4, sort_keys=True,
    ensure_ascii=False)
    outfile.write(retJson)

print(saveFilename + ' file saved')

