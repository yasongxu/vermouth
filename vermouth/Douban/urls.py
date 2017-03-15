# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^get_info_by_id',
        view=views.get_info_by_id,
        name='douban/index/get'
    ),
    url(
        regex=r'^index',
        view=views.index,
        name='douban_index'
    ),
]
