from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Beamline(models.Model):
	name = models.CharField(max_length=100, unique=True)
	notes = models.CharField(max_length=250, blank=True)
	locked = models.BooleanField(default=False)
	updated_date = models.DateTimeField(blank=True, null=True)
	storage_ring_order = models.IntegerField(default=1)

	def __str__(self):
		return self.name
