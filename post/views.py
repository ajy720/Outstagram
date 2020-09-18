from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm

# Create your views here.
from .models import Post


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
        'form': form
    }

    return render(request, "post/postForm.html", context);


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = post.comment_set.all()

    context = {
        'post': post,
        'comments': comment
    }

    return render(request, 'post/detail.html', context)


def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post_like = post.like.all()

    if request.user in post_like:
        flag = False
        post.like.remove(request.user)
    else:
        flag = True
        post.like.add(request.user)

    post.save()

    context = {
        'count': post.like.count(),
        'flag': flag,
    }

    return JsonResponse(context)
