from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


# 게시글 작성 뷰
@login_required(login_url="user:login")
def create_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # 미디어파일이 함께 있으면 같이 인자로 넣어줘야 함.

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post:detail', post.id)

    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, "post/postForm.html", context);


# 게시글 삭제 뷰
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author == request.user:
        post.delete()

    return redirect("feed:main");


# 게시글 수정 뷰
@login_required(login_url="user:login")
def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return redirect('post:detail', post_id=post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # 미디어파일이 함께 있으면 같이 인자로 넣어줘야 함.

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post:detail', post.id)

    else:
        form = PostForm(instance=post)

    context = {
        'form': form
    }

    return render(request, "post/postForm.html", context);


# 게시글 상세 뷰
@login_required(login_url="user:login")
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = post.comment_set.all()

    context = {
        'post': post,
        'comments': comment
    }

    return render(request, 'post/detail.html', context)


# 게시글 좋아요 뷰
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
