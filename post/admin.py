from django.contrib import admin
from .models import Post, PostLike

# Register your models here.

@admin.register(Post)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "author", "like_count", "comment_count")

@admin.register(PostLike)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("post_id", "author")