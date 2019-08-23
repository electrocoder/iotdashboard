# -*- coding: utf-8 -*-
"""
Datas

https://iothook.com/

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
    owner           = models.ForeignKey('auth.User', related_name='ownerdata', on_delete=models.CASCADE)
    channel         = models.ForeignKey(Channel, related_name='channeldata', on_delete=models.CASCADE)
    value_1         = models.CharField(_('Deger 1'), max_length=10, null=True, blank=False)
    value_2         = models.CharField(_('Deger 2'), max_length=10, null=True, blank=False)
    value_3         = models.CharField(_('Deger 3'), max_length=10, null=True, blank=False)
    value_4         = models.CharField(_('Deger 4'), max_length=10, null=True, blank=False)
    value_5         = models.CharField(_('Deger 5'), max_length=10, null=True, blank=False)
    value_6         = models.CharField(_('Deger 6'), max_length=10, null=True, blank=False)
    value_7         = models.CharField(_('Deger 7'), max_length=10, null=True, blank=False)
    value_8         = models.CharField(_('Deger 8'), max_length=10, null=True, blank=False)
    value_9         = models.CharField(_('Deger 9'), max_length=10, null=True, blank=False)
    value_10        = models.CharField(_('Deger 10'), max_length=10, null=True, blank=False)
    enable          = models.BooleanField(_('Aktif et'), default=True)
    remote_address  = models.CharField(_('Ip adres'), max_length=255)
    pub_date        = models.DateTimeField(_('Yayin tarihi'), auto_now=True)

    def __str__(self):
        return self.channel.channel_name
