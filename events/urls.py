from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('members/',include('members.urls'))
]