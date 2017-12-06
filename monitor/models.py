from django.db import models
from django.utils import timezone

# Create your models here.

class Osinfo(models.Model):
	mem_total = models.CharField(max_length=200)
	mem_free = models.CharField(max_length=200)
	mem_percent = models.CharField(max_length=200)
	Hostname  = models.CharField(max_length=200)
	ip  = models.GenericIPAddressField()
	cpu  = models.CharField(max_length=200)
	disk  = models.CharField(max_length=200)
	new_date = models.DateTimeField(default=timezone.now)
	
	class Meta:
		ordering = ('-new_date',)
