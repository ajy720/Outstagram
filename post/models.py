from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField(verbose_name="내용", blank=True, null=True)
    picture = models.ImageField(upload_to='postings/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)


class PostLike(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
