# -*- coding: utf-8 -*-
"""
Iotdashboard project
Django 1.10.1
Python 2.7.6

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
A copy of the License is located at

http://www.apache.org/licenses/
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

for i in range(100):
    data={
        'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463',
        'element_id_1':'a', 'value_1':i*10,
        'element_id_2':'b', 'value_2':i*10,
        # 'element_id_3':'c', 'value_3':i*10,
        # 'element_id_4':'d', 'value_4':i*10,
        # 'element_id_5':'e', 'value_5':i*10,
        # 'element_id_6':'f', 'value_6':i*10,
        # 'element_id_7':'g', 'value_7':i*10,
        # 'element_id_8':'h', 'value_8':i*10,
        # 'element_id_9':'i', 'value_9':i*10,
        # 'element_id_10':'j', 'value_10':i*10,
        }

    data_json = json.dumps(data)
    response = requests.post(url, data=data_json, headers=headers, auth=auth)
    print(response)
    print(response.json())
    time.sleep(10)
