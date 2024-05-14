from django.db import models

# Create your models here.

class userDetails(models.Model):
	Name 		= models.CharField(max_length=100)
	Username 	= models.CharField(max_length=100)
	Passsword 	= models.CharField(max_length=100)
	age 		= models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=100)
	class Meta:
		db_table = 'userDetails'

class admin_details(models.Model):
	aname = models.CharField(max_length=100)
	apass = models.CharField(max_length=100)
	class Meta:
		db_table = 'admin_details'