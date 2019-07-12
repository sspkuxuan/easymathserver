from django.db import models

# Create your models here.
class PinInformation(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=100)
    gotime = models.CharField(max_length=32)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    telephone = models.CharField(max_length=12)
    peoplenum=models.CharField(max_length=3)
    sortgotime = models.IntegerField(2)
    addtime = models.DateTimeField(auto_now=True)

class PinUser(models.Model):
    openid = models.CharField(max_length=100,primary_key=True)
    telephone = models.CharField(max_length=12)