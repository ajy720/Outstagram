from django import forms

from .models import Comment


# UI와 데이터를 주고 받을 댓글 폼 양식
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
