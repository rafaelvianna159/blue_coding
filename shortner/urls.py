from django.contrib import admin
from django.urls import path
from .views import short_main_api

urlpatterns = [
    path('<str:short_url>', short_main_api, name='make url shorter'),
]
