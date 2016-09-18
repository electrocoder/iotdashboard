# -*- coding: utf-8 -*-
"""
Django admin page

https://iothook.com/
"""

from django.contrib import admin

from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'pub_date',)

admin.site.register(Device, DeviceAdmin)
