from django.urls import path
from .views import like_comment, add

app_name = 'comment'

urlpatterns = [
    path("like/<int:comment_id>", like_comment, name="like_comment"),
    path("add/<int:post_id>", add, name="add"),
]