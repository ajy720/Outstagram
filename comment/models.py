from django.db import models
from django.conf import settings
from post.models import Post


# Create your models here.
class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    like_count = models.IntegerField(default=0)


class CommentLike(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
