# -*- coding: utf-8 -*-
"""
Django admin page

https://iothook.com/
"""

from django.contrib import admin

from .models import Data

class DataAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'owner', 'channel', 'enable', 'remote_address', 'pub_date')

admin.site.register(Data, DataAdmin)
