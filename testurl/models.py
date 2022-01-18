# from django.db import models
#
# class test(models.Model):
#     testtext=models.CharField(max_length=100);

#
#
# # Create your models here.
# class CatColor(models.Model):
#     ColorName=models.CharField(max_length=15)
#     def __str__(self):
#         return self.ColorName
#
#
# class Cat(models.Model):
#     CatName = models.CharField(max_length=200)
#     CatColor = models.ForeignKey(CatColor,on_delete=models.DO_NOTHING)
#     # CatColor = models.CharField(max_length=200)
#     CatLocation = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.CatName