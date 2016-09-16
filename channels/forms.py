# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *

class ChannelForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Channel
        exclude = [
            'owner',
            'api_key',
        ]

    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            if i not in ['enable',]:
                self.fields[i].widget.attrs['class'] = 'form-control'
                self.fields[i].widget.attrs['name'] = i
