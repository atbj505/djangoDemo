#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('^tribute/$', views.tribute, name='tribute'),
    url('^current_time/$', views.current_date, name='current_date'),
    url('^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url('^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(),
        name='results'),
    url('^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
