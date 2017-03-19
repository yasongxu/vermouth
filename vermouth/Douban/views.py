# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
from .Utils.context import SkippingPages


@login_required
def get_all():
    pass


def index(request):
    page = int(request.GET.get('page', 1))
    menu_name = request.GET.get('menu_name', "所有图书")
    order = request.GET.get('order_by', "default")
    order_by = "score" if order != "default" else "name"
    menu_contents = ["所有图书", "文化", "科幻", '计算机', "互联网", "诗歌", "都市", "日本", "日本文学", "东野圭吾"]
    # 计算各分类的数量
    menu_counts = list(map(lambda x:
                           {"name": x, "count": Book.objects.filter(menu_type=x).count()},
                           [m for m in menu_contents[1:]]))
    menu_counts.insert(0, {"name": "所有图书", "count": Book.objects.all().count()})
    if menu_name == "所有图书":
        all_books = sorted(Book.objects.all(), key=lambda m: float(m.score), reverse=True)
    else:
        all_books = sorted(Book.objects.filter(menu_type=menu_name), key=lambda m: float(m.score), reverse=True)
    p = SkippingPages(all_books, 20)
    try:
        pages_to_show = p.pages_to_show(page)
        books = p.pages.page(page)
        for i in books:
            if not i.detail:
                books.remove(i)
    except PageNotAnInteger:
        books = p.pages.page(1)
        pages_to_show = p.pages_to_show(1)
    except EmptyPage:
        books = p.pages.page(p.pages.num_pages)
        pages_to_show = p.pages_to_show(p.pages.num_pages)
    print(menu_counts)
    return render(request, 'douban/books/book_list.html',
                  {'books': books, "pages_to_show": pages_to_show, "menu_counts": menu_counts, "menu_name": menu_name,
                   "order_by": order_by})