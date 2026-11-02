# from django.contrib import admin
from django.urls import path
import app_gd.views as views

urlpatterns = [
    path('', views.index),
]
