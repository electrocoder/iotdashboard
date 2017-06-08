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
                  'element_id_1', 'value_1',
                  'element_id_2', 'value_2',
                  'element_id_3', 'value_3',
                  'element_id_4', 'value_4',
                  'element_id_5', 'value_5',
                  'element_id_6', 'value_6',
                  'element_id_7', 'value_7',
                  'element_id_8', 'value_8',
                  'element_id_9', 'value_9',
                  'element_id_10', 'value_10',
                  'remote_address')
