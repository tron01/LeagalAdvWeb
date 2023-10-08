"""
URL configuration for LeagalAdvWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#views
from Administrator import views
from User import user_views
from Advocate import adv_views

urlpatterns = [
     #-------------------------main-----------------------------------#

    path('admin_home/', views.admin_home),
    path('', views.index),
    path('login/', views.login),
    path('adv_register/', views.adv_register),
    path('user_register/', views.user_register),
    


     #-------------------------User-----------------------------------#

    path('user_home/', user_views.user_home),
    path('user_header_footer/', user_views.user_header_footer),
    path('user_bank/', views.user_bank),
    path('user_logout/', user_views.user_logout),

    #-------------------------ADv-----------------------------------#
     path('adv_home/', adv_views.adv_home),
     path('adv_logout/',adv_views.adv_logout),

]
