#!/usr/bin/env python
# -*- coding: utf-8 -*-

from player.models import PlayerProfile
from player.forms import *

def user_created(sender, user, request, **kwargs):
    form = PlayerRegForm(request.POST)
    data = PlayerProfile(user=user)
    data.age = form.data["age"]
    data.save()

from registration.signals import user_registered
user_registered.connect(user_created)