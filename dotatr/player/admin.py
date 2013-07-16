#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from player.models import PlayerProfile

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = PlayerProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]

admin.site.register(User, UserProfileAdmin)