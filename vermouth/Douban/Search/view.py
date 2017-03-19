# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render_to_response, render
from django.db.models import Q
from vermouth.Douban.models import Book


def search_view(request):
    search = request.GET.get('search', "")
    s_type = request.GET.get('s_type', "")
    book = Book.objects.filter(Q(subject__icontains=search) | Q(name__icontains=search) | Q(menu_type__icontains=search))
    if book:
        return render(request, 'douban/books/book_detail.html', {"book": book[0]})
    else:
        return render(request, '500.html')