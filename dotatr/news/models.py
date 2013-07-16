#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class Article(models.Model):
    pub_date = models.DateTimeField("Yayınlanma Tarihi", auto_now_add=True)
    title = models.CharField("Başlık", max_length=200, unique=True)
    content = models.TextField("İçerik")
    publisher = models.ForeignKey(User)
    slideshow = models.BooleanField("Slideshow'da gösterilsin", default=False)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField("Resim", upload_to="article-images/", blank=True, null=True)

    class Meta:
        verbose_name = _('Makale')
        verbose_name_plural = _('Makale')

    def __unicode__(self):
        return self.title

