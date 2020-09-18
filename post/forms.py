from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'content']
        labels = {
            'image': '사진',
            'content': '내용'
        }