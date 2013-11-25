from django.db import models

from django.contrib.auth.models import Game
from django.contrib.auth.models import User

class DonationTarget(models.Model):
	self.month = models.IntegerField()
	self.target = models.IntegerField()
	self.current = models.IntegerField()
	self.end_date = models.DateTimeField("End Date", auto_now_add=True)
	self.start_date = models.DateTimeField("Start Date")
	self.active = models.BooleanField(initial=False)

	def __unicode__(self):
        return self.month