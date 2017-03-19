# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views
from .Books.detail import book_detail
from .Search.view import search_view

urlpatterns = [
    url(
        regex=r'^index',
        view=views.index,
        name='douban_index'
    ),
    url(
        regex=r'^book/(\d{1,10})',
        view=book_detail,
        name='book_detail'
    ),
    url(
        regex=r'^search/',
        view=search_view,
        name='search_view'
    ),
]
