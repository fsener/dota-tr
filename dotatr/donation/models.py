from django.db import models

from django.contrib.auth.models import Game
from django.contrib.auth.models import User

class DonationTarget(models.Model):
	month = models.IntegerField()
	target = models.IntegerField()
	current = models.IntegerField()
	end_date = models.DateTimeField("End Date", auto_now_add=True)
	start_date = models.DateTimeField("Start Date")
	active = models.BooleanField(initial=False)

	def __unicode__(self):
        return self.month