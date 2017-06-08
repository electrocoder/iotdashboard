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

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Data
        fields = ('id', 'owner', 'channel',
                  'value_1',
                  'value_2',
                  'value_3',
                  'value_4',
                  'value_5',
                  'value_6',
                  'value_7',
                  'value_8',
                  'value_9',
                  'value_10',
                  'remote_address')
