"""
Iotdashboard project
Django 3.1
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

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

from devices.models import Device


class Data(models.Model):
    """
    """
    device = models.ForeignKey(Device, related_name='device_data', on_delete=models.CASCADE)
    field_1 = models.CharField(_('Deger 1'), max_length=10, null=True, blank=False)
    field_2 = models.CharField(_('Deger 2'), max_length=10, null=True, blank=False)
    field_3 = models.CharField(_('Deger 3'), max_length=10, null=True, blank=False)
    field_4 = models.CharField(_('Deger 4'), max_length=10, null=True, blank=False)
    field_5 = models.CharField(_('Deger 5'), max_length=10, null=True, blank=False)
    field_6 = models.CharField(_('Deger 6'), max_length=10, null=True, blank=False)
    field_7 = models.CharField(_('Deger 7'), max_length=10, null=True, blank=False)
    field_8 = models.CharField(_('Deger 8'), max_length=10, null=True, blank=False)
    field_9 = models.CharField(_('Deger 9'), max_length=10, null=True, blank=False)
    field_10 = models.CharField(_('Deger 10'), max_length=10, null=True, blank=False)
    api_key = models.CharField(_('Api key'), max_length=200, null=True, blank=True)  # api key
    remote_address = models.CharField(_('Ip adres'), max_length=255)
    pub_date = models.DateTimeField(_('Yayin tarihi'), auto_now=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.device.name
