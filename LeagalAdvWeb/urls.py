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
    path('', views.index),
    path('login/', views.login),
    path('adv_register/', views.adv_register),
    path('user_register/', views.user_register), 
    #------------------------- end main-----------------------------------#

    #-------------------------Admin-----------------------------------#
    path('admin_home/', views.admin_home),
    path('admin_logout/', views.admin_logout),
 
    
    path('user_list/', views.user_list),
    path('user_request/', views.user_request),
    path('user_status/', views.user_status),
    path('user_remove/', views.user_remove),
    path('action_user/', views.action_user),
    
    path('advocate_list/', views.advocate_list),
    path('adv_request/', views.adv_request),
    path('action_adv/', views.action_adv),
    path('adv_status/', views.advocate_status),

    path('ipc_section/', views.ipc_section),
    path('ipc_remove/', views.ipc_remove),
    path('edit_ipc_section',views.edit_ipc),
    
    path('case_category/', views.case_category),
    path('cat_remove/', views.cat_remove),
    path('edit_case_category',views.edit_cat),
    
    path('user_case/',views.user_case),
    path('view_case_list',views.view_case_list),


    path('view_feedback/', views.view_feedback),
    path('approve_pay/',views.approve_pay),
    path('reject_pay/',views.reject_pay),

    #-------------------------Admin End-----------------------------------#

    #-------------------------User-----------------------------------#
    path('user_home/', user_views.user_home),
    path('user_header_footer/', user_views.user_header_footer),
    path('user_bank/', views.user_bank),
    path('user_logout/', user_views.user_logout),

    path('user_ipc/', user_views.user_ipc),
    path('user_about/', user_views.user_about),
    path('user_profile/', user_views.user_profile),
    path('user_cat_list/', user_views.user_cat_list),
    path('user_adv_list/', user_views.user_adv_list),
    path('view_adv/', user_views.view_adv),

    path('add_case/', user_views.add_case),
    path('case_status/', user_views.case_status),
    path('user_view_case_status/', user_views.user_view_case_status),
    path('add_rating/', user_views.add_rating),
    path('change_password/', user_views.change_password),
    
    path('add_doc/', user_views.add_doc),
    path('status1/', user_views.status1),
    path('user_feedback/', user_views.user_feedback),
    path('user_about/', user_views.user_about),

    path('payment1/', user_views.payment1),
    path('payment4/', user_views.payment4),
    
    #-------------------------User End -----------------------------------#

    #-------------------------Advocate End -----------------------------------#
    path('adv_home/', adv_views.adv_home),
    path('adv_logout/',adv_views.adv_logout),
    path('adv_header_footer/', adv_views.adv_header_footer),
    path('adv_home/', adv_views.adv_home),
    path('adv_ipc/', adv_views.adv_ipc),
    path('advocate_profile/', adv_views.advocate_profile),
    path('adv_change_password/', adv_views.adv_change_password),
    path('adv_case_request/', adv_views.adv_case_request),
    path('view_case_request/', adv_views.view_case_request),
    path('status/', adv_views.status),
    path('adv_case_status/', adv_views.adv_case_status),
    path('view_case_status/', adv_views.view_case_status),
    path('case_ipc/', adv_views.case_ipc),
    path('add_fee/', adv_views.add_fee),
    path('add_doc_adv/', adv_views.add_doc),
    path('Case_status1/', adv_views.status1),
    path('adv_feedback/', adv_views.adv_feedback),
    path('rej_com_case/', adv_views.rej_com_case),

    #-------------------------Advocate End -----------------------------------#

]


 