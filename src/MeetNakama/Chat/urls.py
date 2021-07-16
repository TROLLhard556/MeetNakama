from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.Signup, name='Signup'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.Home, name='Home')
]
