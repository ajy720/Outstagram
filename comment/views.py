from django.http import HttpResponse, JsonResponse
from .models import Comment


# Create your views here.
def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment_like = comment.like.all()

    if request.user in comment_like:
        flag = False
        comment.like.remove(request.user)
    else:
        flag = True
        comment.like.add(request.user)

    comment.save()

    context = {
        'count': comment.like.count(),
        'flag': flag,
    }

    return JsonResponse(context)
