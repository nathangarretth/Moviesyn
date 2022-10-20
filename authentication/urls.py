from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('join', views.join, name='join'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]
