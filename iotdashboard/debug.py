# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .settings import DEBUG


def debug(*val):
    """
    :param val:
    :return:
    """
    if DEBUG:
        print(str(val).encode('utf-8'))
    return 0
