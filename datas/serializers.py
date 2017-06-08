# -*- coding: utf-8 -*-
"""
REST Framework

https://iothook.com/
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
