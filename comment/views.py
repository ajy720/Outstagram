from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from post.models import Post
from .forms import CommentForm
from .models import Comment


# 댓글 좋아요 뷰
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


# 댓글 작성 뷰
def add(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = post
        comment.author = request.user

        comment.save()

    return redirect('post:detail', post_id)


# 댓글 삭제 뷰
def delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id);

    if request.user == comment.author:
        comment.delete();

    return redirect("post:detail", post_id=comment.post_id.id)
