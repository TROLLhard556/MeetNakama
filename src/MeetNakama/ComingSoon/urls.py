from django.contrib import admin, auth
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ComingSoon, name='ComingSoon'),

]
