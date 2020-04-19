from django.db import models
from datetime import datetime

# Create your models here.

class Forms(models.Model):
	
	name = models.CharField(max_length=200)
	date = models.DateTimeField(default=datetime.now,blank=True)
	reports = models.CharField(max_length=200)
	team_lead = models.CharField(max_length=200)
	no_of_hours = models.IntegerField(default=0)
	today_progress = models.CharField(max_length=200)
	today_documents = models.FileField(upload_to='documents/%Y/%m/%d/')
	concerns = models.TextField(blank=True)
	next_plan = models.CharField(max_length=200)
	nextplan_documents = models.FileField(upload_to='documents/%Y/%m/%d/')

	def __str__(self):
		return self.name
