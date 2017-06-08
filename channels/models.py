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
        return self.channel_name

    def save(self, *args, **kwargs):
        """
        """
        super(Channel, self).save(*args, **kwargs)

        if not self.channel_name_id:
            name = self.channel_name.replace(u'\u0131', 'i')  # turkce karakter 'ı' icin
            self.channel_name_id = (djslugify(name)).replace('-', '_')
            self.save()
