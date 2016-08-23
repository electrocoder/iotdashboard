#-*- coding: utf-8 -*-
"""
Channel

https://iothook.com/
"""

from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import hashlib, random

from devices.models import Device

class Channel(models.Model):
    """
    Channel
    """
    device          = models.ForeignKey(Device) # Arduino, Rasberry pi ...
    name            = models.CharField(_('isim'), max_length=60, help_text=u"Kanal adını giriniz")
    api_key         = models.CharField(max_length=200) # bu formun url adresi
    pub_date        = models.DateTimeField(auto_now_add=True)
    description     = models.TextField(_('açıklama'), blank=True, max_length=255)
    enable          = models.BooleanField(_('aktif et'), default=True)

    def __unicode__(self):
        """
        """
        return unicode(self.name)


    def save(self, *args, **kwargs):
        """
        """
        super(Channel, self).save(*args, **kwargs)
        if not self.api_key:
            self.api_key = (hashlib.sha1(str(self.pub_date)).hexdigest())[:5] + "-" + (hashlib.sha1(str(random.random())).hexdigest())[:5]
            self.save()