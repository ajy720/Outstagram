from django.urls import path
from .views import main, create_form, detail

app_name = 'post'

urlpatterns = [
    path("", main, name="main"),
    path("create/", create_form, name="create"),
    path("<int:post_id>", detail, name="detail"),
]