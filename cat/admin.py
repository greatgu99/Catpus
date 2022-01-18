from django.contrib import admin
from .models import Cat,CatLocation,CatColor
# Register your models here.

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id','catname','catcolor','catlocation','catlike']

@admin.register(CatColor)
class CatColorAdmin(admin.ModelAdmin):
    list_display = ['colorname']

@admin.register(CatLocation)
class CatLocationAdmin(admin.ModelAdmin):
    list_display = ['locationname']