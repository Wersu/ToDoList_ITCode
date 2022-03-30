from django.contrib import admin
from django.urls import path
import core.views

urlpatterns = [
    path('hello/', core.views.index)
]