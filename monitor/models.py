#_*_ encoding:utf-8 _*__
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

class Maker(models.Model):
	name = models.CharField(max_length=10)
	country = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

class PModel(models.Model):
	maker = models.ForeignKey(Maker,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')
	
	def __unicode__(self):
		return self.name

class Product(models.Model):
	pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE)
	nickname = models.CharField(max_length=15,default='超值手机')
	description = models.TextField(default='暂无说明')
	year = models.PositiveIntegerField(default=2016)
	price = models.PositiveIntegerField(default=0)

	def __unicode(self):
		return self.nickname

class PPhoto(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	description = models.CharField(max_length=20,default='产品照片')
	url = models.URLField(default='http://i.imgur.com/z230eeq.png')
	
	def __unicode__(self):

		return self.description

