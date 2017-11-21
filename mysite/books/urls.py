#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = 'books'

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)

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
        name='requires_login'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]