from django.urls import path
from .views import like_comment

app_name = 'comment'

urlpatterns = [
    path("like/<int:comment_id>", like_comment, name="like_comment"),
]