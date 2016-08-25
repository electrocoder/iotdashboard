#-*- coding: utf-8 -*-
"""
REST Framework

https://iothook.com/
"""

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from models import Data

class UserSerializer(serializers.ModelSerializer):
    """
    """
    datas = serializers.PrimaryKeyRelatedField(many=True, queryset=Data.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'datas')

class DataSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Data
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ('id', 'owner', 'channel', 'name_id', 'value', 'pub_date', 'remote_address',)
