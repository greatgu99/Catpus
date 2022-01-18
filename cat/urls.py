from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.dispatcher),
    # path('<int:page>',views.getcat()),
    path('addpic',views.addpic)
]