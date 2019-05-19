from django.db import models

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class register(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
