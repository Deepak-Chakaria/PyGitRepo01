from django.urls import path
from apps.MyApp1 import views

urlpatterns = [
    path('', views.LoginViewMethod, name='UrlLogin'),
]