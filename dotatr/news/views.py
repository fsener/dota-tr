#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from news.models import Article
from social_auth.models import UserSocialAuth
from django.contrib.auth.models import User

def home(request):
    news = Article.objects.order_by('-pub_date')
    slideshow_news = Article.objects.filter(slideshow=True).order_by('-pub_date')[:5]
    homepage_news = Article.objects.filter(slideshow=False).order_by('-pub_date')[:5]
    matches = ""
    if request.user.is_authenticated():
        try:
            user_data = request.user.social_auth.filter(provider='steam')[0]
        except IndexError:
            user_data = 'nosteam'
    else:
        user_data = 'nologin'
    return render(request, 'news/index.html', {
        'news': news, 
        'slideshow_news': slideshow_news,
        'homepage_news': homepage_news,
        'user_data': user_data,
        })

def show_article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'news/show_article.html', {'article': article})