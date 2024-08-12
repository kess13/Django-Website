from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.login_user , name="login"),
    path('success', views.main, name="success"),
    path('registration', views.register_user, name="registration"),
    path('export_users_data/', views.export_users_data, name="export_users_data"),  # New URL for exporting data
]