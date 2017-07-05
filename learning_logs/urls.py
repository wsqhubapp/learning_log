#!/usr/bin/env python
#_*_ coding:utf-8  _*_
"""定义learning_logs 的URL模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^topics/$', views.topics, name='topics'),
        url(r'^new_topic/$', views.new_topic, name='new_topic'),
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        ##添加新条目的页面
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
        ##编辑条目的页面
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
