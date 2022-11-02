from django.urls import path
from .import views

# URL configuration module
urlpatterns = [
    path('hello/', views.say_hello)
]