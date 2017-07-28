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
=============================

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

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=all'

   auth=('admin', 'Aa1234567890')



   response = requests.get(url, auth=auth)
   data = response.json()
   print data

Get Api Requests.Get last data
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

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=last'

   auth=('admin', 'Aa1234567890')

   response = requests.get(url, auth=auth)
   data = response.json()
   print data

Get Api Requests.Get first data
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

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=first'

   auth=('admin', 'Aa1234567890')

   response = requests.get(url, auth=auth)
   data = response.json()
   print data


Get Api Requests.Get all/first/last data with C#
================================================

C# ile json GET örneği.
Bu örneğe Github: https://github.com/AsocialCoder/CSharp_Webrequest.git adresinden ulaşabilirsiniz.

.. code-block:: c#

   """
   Iot dashboard GET example

   iot-dashboard
   IoT: Platform for Internet of Things

   Iotdashboard source code is available under the MIT License

   Online iot dashboard test and demo http://iotdashboard.pythonanywhere.com

   Online iot dashboard https://iothook.com
   
   You can find project details on our project page https://iothook.com and wiki https://iothook.com
   """

   using System;
   using System.IO;
   using System.Net;

   namespace ConsoleApp1
   {
       class Program
       {
           static void Main(string[] args)
           {
               string url = "";
               url = "http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=last"; // for all data

               var webRequest = (HttpWebRequest)WebRequest.Create(url);
               webRequest.Method = "GET";
               webRequest.ContentType = "application/json";
               webRequest.UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:28.0) Gecko/20100101 Firefox/28.0";
               webRequest.ContentLength = 0;
               string autorization = "admin" + ":" + "Aa1234567890";
               byte[] binaryAuthorization = System.Text.Encoding.UTF8.GetBytes(autorization);
               autorization = Convert.ToBase64String(binaryAuthorization);
               autorization = "Basic " + autorization;
               webRequest.Headers.Add("AUTHORIZATION", autorization);
               var webResponse = (HttpWebResponse)webRequest.GetResponse();
               if (webResponse.StatusCode != HttpStatusCode.OK)
                   Console.WriteLine(webResponse.Headers.ToString());
               using (StreamReader reader = new StreamReader(webResponse.GetResponseStream()))
               {

                   Console.WriteLine(reader.ReadToEnd());
                   reader.Close();
                   webRequest.Abort();
               }

               Console.ReadLine();
           }
       }
   }

    

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

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=last'

   auth=('admin', 'Aa1234567890')

   # response = requests.get(url, auth=auth)
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

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=last'

   auth=('admin', 'Aa1234567890')


   myResponse = requests.get(url, auth=auth, verify=True)
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

  

   url = 'http://iotdashboard.pythonanywhere.com/api/v1/datas/?data=last'

   auth=('admin', 'Aa1234567890')

   myResponse = requests.get(url, auth=auth, verify=True)
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
