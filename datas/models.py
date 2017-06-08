# -*- coding: utf-8 -*-
"""
Datas

https://iothook.com/
"""

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import hashlib, random

from channels.models import Channel


class Data(models.Model):
    """
    """
    owner           = models.ForeignKey('auth.User', related_name='ownerdata')
    channel         = models.ForeignKey(Channel, related_name='channeldata')
    element_1       = models.CharField(_('Element 1'), max_length=20, null=True, blank=True)
    element_id_1    = models.CharField(_('Element ID 1'), max_length=30, null=True, blank=True)
    value_1         = models.CharField(_('Deger 1'), max_length=10, null=True, blank=False)
    element_2       = models.CharField(_('Element 2'), max_length=20, null=True, blank=True)
    element_id_2    = models.CharField(_('Element ID 2'), max_length=30, null=True, blank=True)
    value_2         = models.CharField(_('Deger 2'), max_length=10, null=True, blank=False)
    element_3       = models.CharField(_('Element 3'), max_length=20, null=True, blank=True)
    element_id_3    = models.CharField(_('Element ID 3'), max_length=30, null=True, blank=True)
    value_3         = models.CharField(_('Deger 3'), max_length=10, null=True, blank=False)
    element_4       = models.CharField(_('Element 4'), max_length=20, null=True, blank=True)
    element_id_4    = models.CharField(_('Element ID 4'), max_length=30, null=True, blank=True)
    value_4         = models.CharField(_('Deger 4'), max_length=10, null=True, blank=False)
    element_5       = models.CharField(_('Element 5'), max_length=20, null=True, blank=True)
    element_id_5    = models.CharField(_('Element ID 5'), max_length=30, null=True, blank=True)
    value_5         = models.CharField(_('Deger 5'), max_length=10, null=True, blank=False)
    element_6       = models.CharField(_('Element 6'), max_length=20, null=True, blank=True)
    element_id_6    = models.CharField(_('Element ID 6'), max_length=30, null=True, blank=True)
    value_6         = models.CharField(_('Deger 6'), max_length=10, null=True, blank=False)
    element_7       = models.CharField(_('Element 7'), max_length=20, null=True, blank=True)
    element_id_7    = models.CharField(_('Element ID 7'), max_length=30, null=True, blank=True)
    value_7         = models.CharField(_('Deger 7'), max_length=10, null=True, blank=False)
    element_8       = models.CharField(_('Element 8'), max_length=20, null=True, blank=True)
    element_id_8    = models.CharField(_('Element ID 8'), max_length=30, null=True, blank=True)
    value_8         = models.CharField(_('Deger 8'), max_length=10, null=True, blank=False)
    element_9       = models.CharField(_('Element 9'), max_length=20, null=True, blank=True)
    element_id_9    = models.CharField(_('Element ID 9'), max_length=30, null=True, blank=True)
    value_9         = models.CharField(_('Deger 9'), max_length=10, null=True, blank=False)
    element_10      = models.CharField(_('Element 10'), max_length=20, null=True, blank=True)
    element_id_10   = models.CharField(_('Element ID 10'), max_length=30, null=True, blank=True)
    value_10        = models.CharField(_('Deger 10'), max_length=10, null=True, blank=False)
    enable          = models.BooleanField(_('Aktif et'), default=True)
    remote_address  = models.CharField(_('Ip adres'), max_length=255)
    pub_date        = models.DateTimeField(_('Yayin tarihi'), auto_now=True)

    def __str__(self):
        return self.channel.channel_name
