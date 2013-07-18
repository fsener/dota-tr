#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PlayerProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    has_steam = models.BooleanField("Steam Bağlantısı Yapılmış mı?", default=False, editable=True)
    age = models.IntegerField("Yaş")

    class Meta:
        verbose_name = _('Oyuncu')
        verbose_name_plural = _('Oyuncu')

    def __unicode__(self):
        return self.user
