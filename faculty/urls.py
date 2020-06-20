from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="facultyhome"),
    path("registration/",views.register, name="registration")
    
   ]
