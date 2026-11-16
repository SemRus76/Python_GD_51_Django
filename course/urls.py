# from django.contrib import admin
from django.urls import path
import app_gd.views as views

urlpatterns = [
    path('', views.index),
    path('first_page', views.first_page),
    path('second_page', views.second_page),
    path('json_example', views.json_example),
    path('fruit', views.fruit),
    path('fruit/create', views.fruit_create),
]
