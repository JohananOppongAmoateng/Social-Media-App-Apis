from django.contrib import admin

# Register your models here.
from .models import Post,Repost,Comment

admin.site.register(Post)
admin.site.register(Repost)
admin.site.register(Comment)
