from django.contrib import admin

from boards.models import Post, PostComment

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
