from django.contrib import admin
from django.urls import path, include
from . import views

 

urlpatterns = [          
    path("gatepass/",views.gatepass,name="gatepass"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path('', views.index, name='index'),
    path("complaint/",views.postcomplaint,name="post_complaint"),
    path('del_complaint/<int:pk>/', views.deletecomplaint, name='delete'),

]
