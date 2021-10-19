"""
Iotdashboard project
Django 3.2.8
Python 3.8

Author: Sahin MERSIN

Demo: http://iotdashboard.pythonanywhere.com
Source: https://github.com/electrocoder/iotdashboard

https://iothook.com/
http://mesebilisim.com

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

import binascii
import os

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Device(models.Model):
    """
    Requests for iot device Gateway
    """
    name = models.CharField(_('Cihaz adı'), max_length=60, help_text=_('Cihaz adını giriniz'))
    field_1 = models.CharField(_('Alan 1'), max_length=20, null=True, blank=True)
    field_id_1 = models.CharField(_('Alan ID 1'), max_length=30, null=True, blank=True)
    field_2 = models.CharField(_('Alan 2'), max_length=20, null=True, blank=True)
    field_id_2 = models.CharField(_('Alan ID 2'), max_length=30, null=True, blank=True)
    field_3 = models.CharField(_('Alan 3'), max_length=20, null=True, blank=True)
    field_id_3 = models.CharField(_('Alan ID 3'), max_length=30, null=True, blank=True)
    field_4 = models.CharField(_('Alan 4'), max_length=20, null=True, blank=True)
    field_id_4 = models.CharField(_('Alan ID 4'), max_length=30, null=True, blank=True)
    field_5 = models.CharField(_('Alan 5'), max_length=20, null=True, blank=True)
    field_id_5 = models.CharField(_('Alan ID 5'), max_length=30, null=True, blank=True)
    field_6 = models.CharField(_('Alan 6'), max_length=20, null=True, blank=True)
    field_id_6 = models.CharField(_('Alan ID 6'), max_length=30, null=True, blank=True)
    field_7 = models.CharField(_('Alan 7'), max_length=20, null=True, blank=True)
    field_id_7 = models.CharField(_('Alan ID 7'), max_length=30, null=True, blank=True)
    field_8 = models.CharField(_('Alan 8'), max_length=20, null=True, blank=True)
    field_id_8 = models.CharField(_('Alan ID 8'), max_length=30, null=True, blank=True)
    field_9 = models.CharField(_('Alan 9'), max_length=20, null=True, blank=True)
    field_id_9 = models.CharField(_('Alan ID 9'), max_length=30, null=True, blank=True)
    field_10 = models.CharField(_('Alan 10'), max_length=20, null=True, blank=True)
    field_id_10 = models.CharField(_('Alan ID 10'), max_length=30, null=True, blank=True)
    api_key = models.CharField(_('Api key'), max_length=200)  # api key
    description = models.TextField(_('Açıklama'), blank=True, max_length=255)
    enable = models.BooleanField(_('Aktif et'), default=True)
    remote_address = models.CharField(_('Ip adres'), max_length=255)
    pub_date = models.DateTimeField(_('Yayin tarihi'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = self.generate_key()

        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(12)).decode()
