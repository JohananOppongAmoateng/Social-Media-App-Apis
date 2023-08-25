from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FollowSerializer
from .models import Follow
# Create your views here.
class FollowUser(generics.CreateAPIView):
    """Follow a user"""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()

    def perform_create(self,serializer):
        serializer.save(follower_id=self.request.user)


class ListFollowersAndFollowing(APIView):
    """List the followers and people the current user is following"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        followers = Follow.objects.filter(followed_id=self.request.user) 
        following = Follow.objects.filter(follower_id=self.request.user)

        follower_serializer = FollowSerializer(follower,many=True)
        following_serializer = FollowSerializer(following,many=True)

        data = {
            "followers" : followers,
            "following" : following
        }

        return Response(data,status=status.HTTP_200_OK)
    