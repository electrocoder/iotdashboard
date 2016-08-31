# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *

class DeviceForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Device
        exclude = [
            'slug',
        ]

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable',]:
                self.fields[i].widget.attrs['class'] = 'form-control'
                self.fields[i].widget.attrs['name'] = i
