# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Sensors(models.Model):
	temperature = models.FloatField(default=0)
	humidity = models.FloatField(default=0)
	ps1=models.FloatField(default=0)
	as1=models.CharField(max_length=10)
	ps2=models.FloatField(default=0)
	as2=models.CharField(max_length=10)
	wl=models.FloatField(default=0)
	def __str__(self):
		return str(self.temperature) +' '+ str(self.humidity)

