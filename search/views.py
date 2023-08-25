from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from posts.models import Post
from groups.models import Group
from posts.serializers import PostSerializer
from groups.serializers import GroupSerializer


class SearchView(APIView):
    """
    Class for searching users,posts and groups
    """
    def get(self,request):
        query = request.query_params('q', '')  # Get the search query from the URL parameter
        user_results = User.objects.filter(Q(username__icontains=query))
        post_results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        group_results = Group.objects.filter(Q(name__icontains=query))
        user_serializer = UserSerializer(user_results,many=True)
        post_serializer = PostSerializer(user_results,many=True)
        group_serializer = GroupSerializer(user_results,many=True)

        results = {
            'users': user_serializer.data,
            'posts': post_serializer.data,
            'groups':group_serializer.data
        }

        return Response(results,status=status.HTTP_200_OK)