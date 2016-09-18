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
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'owner', 'channel', 'name_id', 'value', 'pub_date', 'remote_address',)
