from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('signup/', views.signup, name = "signup"),
    #path('login/', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('loginform/', views.loginform, name = "loginform"),
    path('signupform/', views.signupform, name = "signupform"),
]
