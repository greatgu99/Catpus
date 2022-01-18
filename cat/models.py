from django.db import models


# Create your models here.
class CatColor(models.Model):
    colorname=models.CharField(max_length=15)
    def __str__(self):
        return self.colorname

class CatLocation(models.Model):
    locationname=models.CharField(max_length=20)
    def __str__(self):
        return self.locationname

class Cat(models.Model):
    catname = models.CharField(max_length=200)
    catcolor = models.ForeignKey(CatColor,on_delete=models.DO_NOTHING)
    catlocation = models.ForeignKey(CatLocation,on_delete=models.DO_NOTHING)
    catpic= models.CharField(max_length=200)
    catlike = models.IntegerField()

    def __str__(self):
        return self.catname

    class Meta:
        ordering = ['-catlike']