from django.contrib import admin
from django.urls import path
from secondapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('users/',views.users,name="users"),
    path('sign_up/',views.signUpUserForm,name="signUpUserForm"),
]
