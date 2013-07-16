#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def test(request):
    async_url = settings.ASYNC_BACKEND_URL
    return render(request, 'nodetest/test2.html', {'async_url': async_url})

@login_required
def tooltip(request,id):
    user = User.objects.get(username=id)
    return render(request, 'nodetest/tooltip.html', {'user': user})
