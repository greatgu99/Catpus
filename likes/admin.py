from django.contrib import admin
from .models import LikeCat,LikeMoments
# Register your models here.

@admin.register(LikeMoments)
class LikeMomentsAdmin(admin.ModelAdmin):
    list_display = ['person','moments']


@admin.register(LikeCat)
class LikeCatAdmin(admin.ModelAdmin):
    list_display = ['person','cat']