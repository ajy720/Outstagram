import pdb

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.


@login_required(login_url="user:login")
def main(request):

    return render(request, "base.html");


@login_required(login_url="user:login")
def create_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # 미디어파일이 함께 있으면 같이 인자로 넣어줘야 함.

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post:main')

    else:
        form = PostForm()

    context = {
        'form' : form
    }

    return render(request, "post/postForm.html", context);

