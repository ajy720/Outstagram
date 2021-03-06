from django.conf import settings
from django.db import models

from post.models import Post
from user.models import User


# 댓글 모델
class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    like = models.ManyToManyField(User, related_name='comment_like', blank=True)
