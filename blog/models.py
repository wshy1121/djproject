# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)

    def __str__(self):
        return self.title
