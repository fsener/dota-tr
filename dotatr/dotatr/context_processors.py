#!/usr/bin/env python
# -*- coding: utf-8 -*-
from news.models import Article

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def block_contents(request):

    latest_news = Article.objects.order_by('-pub_date')[:5]

    return {'latest_news': latest_news}

