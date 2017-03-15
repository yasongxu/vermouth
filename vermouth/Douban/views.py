# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Book
import json


@login_required
def get_all():
    pass


def get_info_by_id(request):
    info = Book.objects.get(id=1000).subject_url
    return HttpResponse(json.dumps(100))


def index(request):
    return render_to_response('douban/books/book_list.html',{},RequestContext(request))