from django.urls import path,include
from . import views
from .views import login

urlpatterns = [
    path('/home', views.home, name='home_path'),

    path('',login,name='login'),
]
