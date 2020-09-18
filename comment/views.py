from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment


# Create your views here.
def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment_like = comment.like.all()

    if request.user in comment_like:
        comment.like.remove(request.user)
    else:
        comment.like.add(request.user)


    comment.save()


    return HttpResponse(True)
    # if request.user in comment_like:
    #     pass
    # else:
