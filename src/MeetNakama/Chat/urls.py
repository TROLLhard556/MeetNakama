from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.Signup, name='Signup'),
    path('', include('django.contrib.auth.urls')),
    path('', views.Home, name='Home'),
    path('chat/', views.Chat, name='Chat'),
    path('settings/', views.Settings, name='Settings')
]
