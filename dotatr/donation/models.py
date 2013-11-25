from django.db import models

class DonationTarget(models.Model):
	month = models.IntegerField()
	target = models.IntegerField()
	current = models.IntegerField()
	end_date = models.DateTimeField("End Date", auto_now_add=True)
	start_date = models.DateTimeField("Start Date")
	active = models.BooleanField(default=False)