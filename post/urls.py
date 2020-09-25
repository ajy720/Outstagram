from django.urls import path
from .views import main, create_form, detail, like_post, delete

app_name = 'post'

urlpatterns = [
    path("", main, name="main"),
    path("create/", create_form, name="create"),
    path("delete/<int:post_id>", delete, name="delete"),
    path("<int:post_id>", detail, name="detail"),
    path("like/<int:post_id>", like_post, name="like_post"),
]