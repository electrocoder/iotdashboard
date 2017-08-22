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
from django.utils.translation import ugettext_lazy as _


FORM_ELEMENTS = (
    ("text", "text"),
    ("number", "number"),
)

class Channel(models.Model):
    """
    Requests for iot device
    """
    owner          = models.ForeignKey('auth.User', related_name='ownerchannel')
    channel_name   = models.CharField(_('Kanal adı'), max_length=60, help_text=_('Kanal adını giriniz'))
    channel_name_id= models.CharField(_('Kanal ID'), max_length=90, null=True, blank=True)
    element_1       = models.CharField(_('Element 1'), max_length=20, null=True, blank=True)
    element_id_1    = models.CharField(_('Element ID 1'), max_length=30, null=True, blank=True)
    element_2       = models.CharField(_('Element 2'), max_length=20, null=True, blank=True)
    element_id_2    = models.CharField(_('Element ID 2'), max_length=30, null=True, blank=True)
    element_3       = models.CharField(_('Element 3'), max_length=20, null=True, blank=True)
    element_id_3    = models.CharField(_('Element ID 3'), max_length=30, null=True, blank=True)
    element_4       = models.CharField(_('Element 4'), max_length=20, null=True, blank=True)
    element_id_4    = models.CharField(_('Element ID 4'), max_length=30, null=True, blank=True)
    element_5       = models.CharField(_('Element 5'), max_length=20, null=True, blank=True)
    element_id_5    = models.CharField(_('Element ID 5'), max_length=30, null=True, blank=True)
    element_6       = models.CharField(_('Element 6'), max_length=20, null=True, blank=True)
    element_id_6    = models.CharField(_('Element ID 6'), max_length=30, null=True, blank=True)
    element_7       = models.CharField(_('Element 7'), max_length=20, null=True, blank=True)
    element_id_7    = models.CharField(_('Element ID 7'), max_length=30, null=True, blank=True)
    element_8       = models.CharField(_('Element 8'), max_length=20, null=True, blank=True)
    element_id_8    = models.CharField(_('Element ID 8'), max_length=30, null=True, blank=True)
    element_9       = models.CharField(_('Element 9'), max_length=20, null=True, blank=True)
    element_id_9    = models.CharField(_('Element ID 9'), max_length=30, null=True, blank=True)
    element_10      = models.CharField(_('Element 10'), max_length=20, null=True, blank=True)
    element_id_10   = models.CharField(_('Element ID 10'), max_length=30, null=True, blank=True)
    api_key        = models.CharField(_('Api key'), max_length=200) # api
    description    = models.TextField(_('Açıklama'), blank=True, max_length=255)
    enable         = models.BooleanField(_('Aktif et'), default=True)
    remote_address = models.CharField(_('Ip adres'), max_length=255)
    pub_date       = models.DateTimeField(_('Yayin tarihi'), auto_now=True)

    def __str__(self):
        return self.owner.username

    def save(self, *args, **kwargs):
        """
        """
        if not self.channel_name_id:
            name = self.channel_name.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.channel_name_id = (djslugify(name)).replace('-', '_')

        if not self.element_id_1:
            name = self.element_1.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_1 = (djslugify(name)).replace('-', '_')

        if not self.element_id_2:
            name = self.element_2.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_2 = (djslugify(name)).replace('-', '_')

        if not self.element_id_3:
            name = self.element_3.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_3 = (djslugify(name)).replace('-', '_')

        if not self.element_id_4:
            name = self.element_4.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_4 = (djslugify(name)).replace('-', '_')

        if not self.element_id_5:
            name = self.element_5.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_5 = (djslugify(name)).replace('-', '_')

        if not self.element_id_6:
            name = self.element_6.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_6 = (djslugify(name)).replace('-', '_')

        if not self.element_id_7:
            name = self.element_7.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_7 = (djslugify(name)).replace('-', '_')

        if not self.element_id_8:
            name = self.element_8.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_8 = (djslugify(name)).replace('-', '_')

        if not self.element_id_9:
            name = self.element_9.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_9 = (djslugify(name)).replace('-', '_')

        if not self.element_id_10:
            name = self.element_10.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.element_id_10 = (djslugify(name)).replace('-', '_')

        super(Channel, self).save(*args, **kwargs)
