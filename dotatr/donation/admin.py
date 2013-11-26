from django.contrib import admin
from donation.models import *

class DonationTargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(DonationTarget, DonationTargetAdmin)

class DonorLevelAdmin(admin.ModelAdmin):
    pass
admin.site.register(DonorLevel, DonorLevelAdmin)