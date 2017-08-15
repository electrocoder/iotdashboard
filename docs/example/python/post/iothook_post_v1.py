
import requests
import json
import urllib
import random
import pprint
import time


headers = {'Content-type': 'application/json'}
url = 'http://localhost:8000/api/v1/datas/'

auth=('admin', 'Aa1234567890')

for i in range(10):
    data={
        'api_key':'c43109a9743547f88f5e53eec897581f46cda59c',
        'element_1':'isi', 'value_1':i*10,
        'element_2':'isik', 'value_2':i*20,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(1)