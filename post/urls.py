from django.urls import path
from .views import create_form, detail, like_post, delete, modify

app_name = 'post'

urlpatterns = [
    path("create/", create_form, name="create"),
    path("delete/<int:post_id>", delete, name="delete"),
    path("modify/<int:post_id>", modify, name="modify"),
    path("<int:post_id>", detail, name="detail"),
    path("like/<int:post_id>", like_post, name="like_post"),
]