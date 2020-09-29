from django.urls import path
from .views import main, search

app_name = 'feed'

urlpatterns = [
    path("", main, name="main"),
    path("search", search, name="search"),

]