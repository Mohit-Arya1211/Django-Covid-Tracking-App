from myApp.views import helloworld
from django.contrib import admin
from django.urls import path
from .views import helloworld

urlpatterns = [
    path('', helloworld),
]
