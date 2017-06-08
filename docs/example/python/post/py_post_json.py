# -*- coding: utf-8 -*-
"""
Iot dashboard POST example

iot-dashboard
IoT: Platform for Internet of Things

Iotdashboard source code is available under the MIT License

Online iot dashboard test and demo http://ihook.xyz

Online iot dashboard https://iothook.com

You can find project details on our project page https://iothook.com and wiki https://iothook.com
"""


import requests
import json
import time


headers = {'Content-type': 'application/json'}
url = 'http://localhost:8000/api/v1/datas/'

auth=('admin', 'Aa1234567890')

for i in range(100):
    data={
        'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463',
        'value_1':i*10,
        'value_2':i*10,
        'value_3':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)
