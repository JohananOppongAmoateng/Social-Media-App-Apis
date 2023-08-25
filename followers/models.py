from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Follow(models.Model):
    """Model for the relationship between users and 
    their followers and people they follow
    """
    follower_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="follower")
    followed_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="following") 
