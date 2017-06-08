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
import urllib
import urllib2
import random
import pprint
import time


headers = {'Content-type': 'application/json'}
url = 'http://localhost:8000/api/v1/datas/'

auth=('admin', 'Aa1234567890')

for i in range(10):
    data={
        'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463',
        'element_id_1':'a', 'value_1':i*10,
        'element_id_2':'b', 'value_2':i*10,
        'element_id_3':'c', 'value_3':i*10,
        'element_id_4':'d', 'value_4':i*10,
        'element_id_5':'e', 'value_5':i*10,
        'element_id_6':'f', 'value_6':i*10,
        'element_id_7':'g', 'value_7':i*10,
        'element_id_8':'h', 'value_8':i*10,
        'element_id_9':'i', 'value_9':i*10,
        'element_id_10':'j', 'value_10':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(5)
