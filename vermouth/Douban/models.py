# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import requests
import json
import traceback
from .Utils.convert import is_json


@python_2_unicode_compatible
class Book(models.Model):
    subject = models.CharField(u'豆瓣subject', blank=True, null=True, max_length=255)
    name = models.CharField(u'图书名', blank=True, null=True, max_length=255)
    content = models.TextField(u'图书详情', blank=True, null=True)
    menu_type = models.CharField(u'图书分类', blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name

    @property
    def subject_url(self):
        url = "https://book.douban.com/subject/{0}/".format(self.subject)
        return url

    @property
    def detail(self):
        try:
            json_judge = is_json(self.content)
            if json_judge and "rating" in json_judge:
                content = json_judge
            else:
                url = "https://api.douban.com/v2/book/{0}".format(self.subject)
                data = requests.get(url, timeout=3).content
                print(data)
                self.content = data
                self.save()
                content = json.loads(data)
            return content
        except:
            traceback.print_exc()
            return {}

    @property
    def score(self):
        json_judge = is_json(self.content)
        if json_judge and "rating" in json_judge:
            return json_judge["rating"]["average"]
        else:
            return "8.8"

    def to_dict(self):
        return dict([(attr, str(getattr(self, attr))) for attr in [f.name for f in self._meta.fields]])

    class Meta:
        db_table = 'douban_book'
        ordering = ("-id",)
        verbose_name = u'图书信息表'
