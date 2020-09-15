from django.contrib import admin
from .models import Comment, CommentLike

# Register your models here.

@admin.register(Comment)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("post_id", "content", "author", "like_count")

@admin.register(CommentLike)
class AnswerAdmin(admin.ModelAdmin):
    pass