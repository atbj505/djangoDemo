#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^meta/$', views.meta, name='meta')
]
