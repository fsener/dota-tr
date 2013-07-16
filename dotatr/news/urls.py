#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.home, name='news_home'),
    url(
    r'^(?P<slug>[^\.]+)', 
    views.show_article, 
    name='show_article'),
)