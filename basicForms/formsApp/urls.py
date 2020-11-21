from django.urls import path
from formsApp import views


urlpatterns = [
    path('', views.index , name="index"),
    path('form/', views.form_view, name="form_view")
]