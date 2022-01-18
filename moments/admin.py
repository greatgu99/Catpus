from django.contrib import admin
from .models import Moments
# Register your models here.

@admin.register(Moments)
class MomentsAdmin(admin.ModelAdmin):
    list_display = ['id','cat','content','person','like','createdtime']
