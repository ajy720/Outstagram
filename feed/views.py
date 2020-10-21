from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from post.models import Post
from user.models import User


# 메인(타임라인(피드)) 뷰
@login_required(login_url="user:login")
def main(request):
    user = get_object_or_404(User, id=request.user.id)

    followings = user.get_following()

    posts = Post.objects.filter(author__in=[user for user in followings])

    context = {
        "posts": posts
    }

    return render(request, "feed/timeline.html", context);


# 검색 뷰
@login_required(login_url="user:login")
def search(request):
    keywords = request.POST['search'].split()

    users = []
    posts = []

    for word in keywords:
        users = User.objects.filter(username__contains=word)
        posts = Post.objects.filter(content__contains=word)

    context = {
        'posts': posts,
        'users': users,
    }

    return render(request, 'feed/search.html', context)
