from django import forms

from .models import Post


# UI와 데이터를 주고 받을 게시글 폼 양식
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'content']
        labels = {
            'image': '사진',
            'content': '내용'
        }
