# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render_to_response, render
from vermouth.Douban.models import Book


def book_detail(request, subject):
    # name = request.GET.get('name', "")
    # subject = request.GET.get('subject', "")
    book = Book.objects.filter(subject=subject)
    if book:
        return render(request, 'douban/books/book_detail.html', {"book": book[0]})
    else:
        return render(request, '500.html')