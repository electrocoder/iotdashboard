#-*- coding: utf-8 -*-
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
    Requests for iot device
    """
    owner          = models.ForeignKey('auth.User', related_name='datas')
    remote_address = models.CharField(_('ip adres'), max_length=255)
    channel        = models.ForeignKey(Channel)
    name_id        = models.CharField(_('isim id'), max_length=70, null=False, blank=False)
    value          = models.CharField(_('deger'), max_length=10, null=False, blank=False)
    pub_date       = models.DateTimeField(_('yayin tarihi'), auto_now=True)

    def __unicode__(self):
        return unicode(self.channel.name)

