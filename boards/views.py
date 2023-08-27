import typing

from django.shortcuts import render, get_object_or_404
from boards.models import Post, PostComment

if typing.TYPE_CHECKING:
    from django.http import HttpRequest
    from django.shortcuts import HttpResponse
    from django.db.models import QuerySet


def index(request) -> 'HttpResponse':
    posts: 'QuerySet[Post]' = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'boards/index.html', context)


def detail(request: 'HttpRequest', post_id: int) -> 'HttpResponse':
    post: Post = get_object_or_404(Post, pk=post_id)
    context = {
        "post": post
    }
    return render(request, 'boards/detail.html', context)
