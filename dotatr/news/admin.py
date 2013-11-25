#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import Article
from donation.models import DonationTarget
from django.template.defaultfilters import slugify

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug','publisher',)
    list_display = ('title', 'publisher','pub_date','slug')
    def save_model(self, request, obj, form, change):
        obj.publisher = request.user
        altered_title = obj.title.replace(u"ı", "i")
        obj.slug = slugify(altered_title)
        obj.save()


admin.site.register(Article, ArticleAdmin)

class DonationTargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(DonationTarget, DonationTargetAdmin)