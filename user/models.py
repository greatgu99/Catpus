from django.db import models

# Create your models here.
class User(models.Model):
    personid = models.CharField(max_length=200)
    avatarurl = models.CharField(max_length=200)
    city=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    gender=models.IntegerField(blank=True)
    nickname=models.CharField(max_length=200)
    province=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.nickname