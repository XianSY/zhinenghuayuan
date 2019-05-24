from django.db import models

# Create your models here.
class userRegister(models.Model):
    username=models.CharField(max_length=20)
    useremail=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username
class ardiunoData(models.Model):
    Humidity=models.FloatField(default=0)
    Temperature=models.FloatField(default=0)
    Humidity=models.FloatField(default=0)
    Soil_1=models.FloatField(default=0)
    Soil_2=models.FloatField(default=0)
    Soil_3=models.FloatField(default=0)
    Soil_4=models.FloatField(default=0)
    Avg_soil=models.FloatField(default=0)
