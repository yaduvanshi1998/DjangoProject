"""
URL configuration for LoginSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Loginify import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name="login"),
    path('user-details/', views.get_all_userdetails, name='user-details'),
    path('user-by-email/<str:Email>/', views.get_user_by_email, name='user-by-email'),
    path('update-user/<str:Username>/', views.update_user_details, name = 'update-user'),
    path('delete-user/<str:Email>/', views.delete_user_by_email, name='delete-user')
]
