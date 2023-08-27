import typing
from django.shortcuts import render
from boards import models

if typing.TYPE_CHECKING:
    from django.shortcuts import HttpResponse
    from django.db.models import QuerySet


def index(request) -> 'HttpResponse':
    posts: 'QuerySet[models.Post]' = models.Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'boards/index.html', context)
