from django.db import models
from cat.models import Cat
from moments.models import Moments
from user.models import User
# Create your models here.
class LikeMoments(models.Model):
    person = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    moments = models.ForeignKey(Moments, on_delete=models.DO_NOTHING)
    # def __str__(self):
    #     return

class LikeCat(models.Model):
    person = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cat = models.ForeignKey(Cat, on_delete=models.DO_NOTHING)