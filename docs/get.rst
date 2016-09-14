.. iotHook documentation master file, created by
   sphinx-quickstart on Tue Apr 12 04:35:14 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GET Web API
===========

Iotdashboard REST framework Web API ile güçlendirilmiştir.

GET Yapısı
==========

.. code-block:: bash

   http http://127.0.0.1:8000/api/v1/DATA_ID

GET Api
=======

.. code-block:: bash

   http http://127.0.0.1:8000/api/v1/11

GET işlemi başarılı ise JSON olarak veri döner.

.. code-block:: bash

   $ http http://127.0.0.1:8000/api/v1/11
   HTTP/1.0 200 OK
   Allow: GET, PUT, DELETE, HEAD, OPTIONS
   Content-Language: tr
   Content-Type: application/json
   Date: Sat, 03 Sep 2016 23:36:19 GMT
   Server: WSGIServer/0.1 Python/2.7.12
   Vary: Accept, Accept-Language, Cookie
   X-Frame-Options: SAMEORIGIN

   {
       "channel": 6,
       "id": 11,
       "name_id": "test",
       "owner": 2,
       "pub_date": "2016-09-03T23:16:33.314292Z",
       "remote_address": "127.0.0.1&HTTPie/0.9.6&HTTP/1.1",
       "value": "1"
   }

GET başarısız ise şu mesaj alınır.

.. code-block:: bash

    $ http http://127.0.0.1:8000/api/v1/999
    HTTP/1.0 404 Not Found
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    Content-Language: tr
    Content-Type: application/json
    Date: Sat, 03 Sep 2016 23:38:44 GMT
    Server: WSGIServer/0.1 Python/2.7.12
    Vary: Accept, Accept-Language, Cookie
    X-Frame-Options: SAMEORIGIN

    {
        "detail": "Bulunamadı."
    }

Get Api Requests.Get all data
==============================

Python ile GET örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests

   API_KEY = "0cd76eb-5f3b179"
   url = 'http://localhost:8000/api/v1/datas/' + API_KEY

   response = requests.get(url, auth=('admin', 'Aa12345**'))
   data = response.json()
   print data

Get Api Requests.Get detail
===========================

Python ile GET örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests

   API_KEY = "0cd76eb-5f3b179"
   url = 'http://localhost:8000/api/v1/datas/7/' + API_KEY

   response = requests.get(url, auth=('admin', 'password'))
   data = response.json()
   print data

Get Api Requests.Get json graph
===============================

Python ile json GET örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests

   API_KEY = "0cd76eb-5f3b179"
   url = 'http://localhost:8000/api/v1/datas/' + API_KEY

   response = requests.get(url, auth=('admin', 'Aa12345**'))
   data = response.json()
   print data

Get Api Requests.Get py_get_json_to_py2neo
==========================================

Python ile json GET örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests

   API_KEY = "0cd76eb-5f3b179"
   url = 'http://localhost:8000/api/v1/datas/' + API_KEY

   # response = requests.get(url, auth=('admin', 'Aa12345**'))
   # data = response.json()
   # print data


   # from py2neo import Graph, Path
   # graph = Graph()
   #
   # tx = graph.cypher.begin()
   # for name in ["Alice", "Bob", "Carol"]:
   #     tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
   # alice, bob, carol = [result.one for result in tx.commit()]
   #
   # friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
   # graph.create(friends)

Get Api Requests.Get py_get_requests
====================================

Python ile status_code GET örneği.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests
   import httplib, urllib
   from requests.auth import HTTPDigestAuth
   import json
   import matplotlib.pyplot as plt

   API_KEY = "c791e11-d9ab779"

   url = 'http://localhost:8000/api/v1/datas/' + API_KEY

   myResponse = requests.get(url, auth=('iottestuser', 'iot12345**'), verify=True)
   print (myResponse.status_code)

   if(myResponse.ok):
       jData = json.loads(myResponse.content)
       print jData
   else:
       myResponse.raise_for_status()

Get Api Requests.Get py_get_requests_matplotlib
===============================================

Python ile json GET örneği. Matplotlib ile grafik çizimi.
Bu örneğe `Github`_ adresinden ulaşabilirsiniz.

.. _Github: https://goo.gl/5WZ91D

.. code-block:: python

   # -*- coding: utf-8 -*-
   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://ihook.xyz

   Online iot dashboard https://iothook.com

   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   import requests
   import httplib, urllib
   from requests.auth import HTTPDigestAuth
   import json
   import matplotlib.pyplot as plt

   API_KEY = "c791e11-d9ab779"

   url = 'http://localhost:8000/api/v1/datas/' + API_KEY

   myResponse = requests.get(url, auth=('iottestuser', 'iot12345**'), verify=True)
   print (myResponse.status_code)

   d= []

   if(myResponse.ok):
       jData = json.loads(myResponse.content)
       for i in jData:
           print i['value']
           d.append(i['value'])
       plt.plot(d)
       plt.show()
   else:
       myResponse.raise_for_status()
