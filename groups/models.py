from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Group(models.Model):
    """Model for the Group"""
    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}" 


class GroupMember(models.Model):
    """Model for the Group Members and groups they have joined"""
    group_id = models.ForeignKey(Group,on_delete=models.CASCADE)
    member_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member_id.}"


