from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.dispatcher),
    path('testurl',views.testurl)
]