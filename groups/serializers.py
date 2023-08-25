from rest_framework import serializers
from .models import Group,GroupMember

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name","created_by",]


class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = "__all__"
