from django.contrib import admin
from news.models import Article

class DonationTargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(DonationTarget, DonationTargetAdmin)