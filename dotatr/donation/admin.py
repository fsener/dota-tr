from django.contrib import admin
from donation.models import DonationTarget

class DonationTargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(DonationTarget, DonationTargetAdmin)