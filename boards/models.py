from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    text = models.CharField(verbose_name='내용', max_length=512)
    like_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(verbose_name="게시일")

    def __str__(self):
        return self.title[:10]

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(verbose_name="내용", max_length=256)

    def __str__(self):
        return self.text[:10]
