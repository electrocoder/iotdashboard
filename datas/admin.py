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

from django.contrib import admin

from .models import Data

class DataAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'owner', 'channel', 'enable', 'remote_address', 'pub_date')

admin.site.register(Data, DataAdmin)
