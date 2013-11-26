from django.db import models
from django.contrib.auth.models import User

class DonationTarget(models.Model):
	month = models.IntegerField()
	target = models.IntegerField()
	current = models.IntegerField()
	end_date = models.DateTimeField("End Date", auto_now_add=True)
	start_date = models.DateTimeField("Start Date")
	active = models.BooleanField(default=False)

class Donation(models.Model):
	user_id = models.ForeignKey(User)
	amount = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	game = models.CharField(max_length=50)
	#maybe currency?

class DonorLevel(models.Model):
	lower = models.IntegerField()
	upper = models.IntegerField()
	desc = models.CharField(max_length=100)