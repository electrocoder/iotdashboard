# -*- coding: utf-8 -*-
"""
Channels admin page

https://iothook.com/
"""

from django.contrib import admin

from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'owner', 'channel_name', 'channel_name_id', 'api_key', 'enable', 'remote_address')

admin.site.register(Channel, ChannelAdmin)
