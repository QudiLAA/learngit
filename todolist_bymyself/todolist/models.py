#coding:utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Item(models.Model):
    content=models.CharField(max_length=180,verbose_name=u'事项内容')
    is_done=models.BooleanField(default=False,verbose_name=u'事项状态')
    pub_date=models.DateField(auto_now_add=True,verbose_name=u'事项时间')
    class Meta:
        verbose_name='待办事项'
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.content




