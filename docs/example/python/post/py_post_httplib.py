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

import httplib, urllib
from base64 import b64encode

userAndPass = b64encode(b"admin:Aa1234567890").decode("ascii")
headers = {'Authorization':'Basic %s' % userAndPass}

auth=('admin', 'Aa1234567890')

datas = urllib.urlencode({'element_id_1':'a', 'value_1':10, 'api_key':'311b9c68f7e64bdfb77aab1e4d53aaf04378a463'})

conn = httplib.HTTPConnection("localhost", 8000)
conn.request("POST", "/api/v1/datas/", datas, headers)

response = conn.getresponse()

print response.status, response.reason

print response.read()

