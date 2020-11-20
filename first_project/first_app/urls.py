from django.urls import path
from first_app import views


# Urls for first_app application
urlpatterns = [
    path('',views.index,name="index"),
    path('first_app/',views.first_app,name="first_app"),
]    