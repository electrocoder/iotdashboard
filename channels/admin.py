# -*- coding: utf-8 -*-
"""
Django admin page

https://iothook.com/
"""

from django.contrib import admin

from .models import Channel

class ChannelAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('device', 'name',)

admin.site.register(Channel, ChannelAdmin)
