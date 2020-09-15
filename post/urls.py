from django.urls import path
from .views import main

app_name = 'post'

urlpatterns = [
    path("", main, name="main")
]