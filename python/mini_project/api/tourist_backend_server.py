from pymongo import mongo_client
from PIL import Image
import os
import json

BASE_DIR = os.path.dirname(os.path.relpath("./"))
secret_file = os.path.join(BASE_DIR, "../../secret.json")
TEST_DIR = '../test/'

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    
    except KeyError:
        errorMsg = "Set the {} enviroment variable.".format(setting)
        return errorMsg

MONGO_HOST = get_secret('Mongo_Host')

client = mongo_client.MongoClient(MONGO_HOST)
mydb = client['test']

mycol = mydb.graphs

# img = Image.open('../graph/Graph01.png')
# img.show()