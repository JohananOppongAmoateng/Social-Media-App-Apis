from rest_framework import serializers
from .models import Post,Repost,Comment

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(method_name="get_likkes_count")
    class Meta:
        model = Post
        fields = "__all__"

    def get_likes_count(self,obj):
        return obj.likes.count()
        
class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

