
import requests
import json
import urllib
import random
import pprint
import time


headers = {'Content-type': 'application/json'}
url = 'http://iotdashboard.pythonanywhere.com/api/v1.1/datas/'

for i in range(10):
    data={
        'api_key':'9aa7a1428aba49df8d51d94c2e75e8b049108da3',
        'value_1':i*10,
        'value_2':i*20,
        'value_3':i*30,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers)
    print(response)
    print(response.json())
    time.sleep(1)
