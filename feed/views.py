from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from user.models import User
from post.models import Post

# Create your views here.

@login_required(login_url="user:login")
def main(request):
    user = get_object_or_404(User, id=request.user.id)

    followings = user.following.all()
    posts = Post.objects.filter(author__in=followings)

    context = {
        "posts": posts
    }

    return render(request, "feed/timeline.html", context);
