from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    """
    Post Model
    """
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="owner")
    text = models.TextField(max_length=400)
    image = models.ImageField(null=True)
    video = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(get_user_model(),related_name="users_liked")

class Repost(models.Model):
    """
    Repost Model
    """
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    original_post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

# class Like(models.Model):
#     user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
#     post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
#     created_at = models.DateTimeField()

    
class Comment(models.Model):
    """
    Comment Model
    """
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    text = models.CharField(max_length = 100)
    created_at = models.DateTimeField()




 