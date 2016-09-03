# -*- coding: utf-8 -*-
"""
Django admin page

https://iothook.com/
"""

from django.contrib import admin

from models import Element

class ElementAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('channel', 'name',)

admin.site.register(Element, ElementAdmin)
