from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path("next/", views.Next, name="next"),
]
