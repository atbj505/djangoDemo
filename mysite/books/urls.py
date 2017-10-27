#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^meta/$', views.meta, name='meta'),
    url('^search_form/$', views.search_form, name='search_form'),
    url('^search/$', views.search, name='search'),
    url('^contact/$', views.contact, name='contact'),
    url('^contact/thanks/$', views.contact_thanks, name='contact_thanks'),
    url('^view1/$',
        views.requires_login(views.my_view1),
        name='requires_login'),
    url('^view2/$',
        views.requires_login(views.my_view2),
        name='requires_login')

]
