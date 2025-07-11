"""
URL configuration for janaproject project.

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
from app1.views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='home'),
    path('about/',aboutpage,name='about'),
    path('course/',coursepage,name='course'),
    path('create/',createpage,name='create'),
    path('read/',readpage,name='read'),
    path('update/<id>/',updatepage,name='update'),
    path('delete/<id>/',deletepage,name='delete'),
    #classy views:
    path('reg/',create.as_view(),name='reg'),
    path('display/',login_required(display.as_view()),name='displaypage'),
    path('edit/<id>/',login_required(edit.as_view()),name='edit'),
    path('remove/<id>/',login_required(remove.as_view()),name='remove'),

    #Authentication
    path('signup/',signuppage,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('staff/',staffpage,name='staff'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),

    #Email:
    path('password_reset/',PasswordResetView.as_view(template_name='reset.html'),name='password_reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(template_name='done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='complete.html'),name='password_reset_complete'),

    ]

