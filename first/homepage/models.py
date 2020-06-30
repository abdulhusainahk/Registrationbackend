from django.db import models

# Create your models here.
# Login and Registration Models

class LogIn(models.Model):
	Username=models.CharField(max_length=30,primary_key=True)
	Password=models.CharField(max_length=8)
	class Meta:
		db_table='login'


class Registration(models.Model):
	Name=models.CharField(max_length=30,primary_key=True)
	Email=models.EmailField(max_length=40)
	Phone=models.IntegerField()
	Username=models.CharField(max_length=10)
	UserId=models.CharField(max_length=10)
	Password=models.CharField(max_length=8)
	
	class Meta:
		db_table='register'

