
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
# Create your views here.
from .models import Post,Comment,Repost
from .serializers import PostSerializer,RepostSerializer,CommentSerializer
from .permissions import IsOwner

class CreatePostView(generics.CreateAPIView):
    "Creating posts"
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class UpdatePostView(generics.UpdateAPIView):
    """Updating posts"""
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwner,permissions.IsAuthenticated]

class DeletePostView(generics.DestroyAPIView):
    """Deleting posts"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_class = [IsOwner,permissions.IsAuthenticated]

class RepostView(generics.CreateAPIView):
    """Reposting posts"""
    serializer_class = RepostSerializer
    queryset = Repost.objects.all()
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user,original_post_id=self.kwargs.get("original_post_id"))

class LikePostView(APIView):
    """Liking posts"""
    permission_classes = [permissions.IsAuthenticated]
    def put(self,request,pk):
        posts = Post.objects.get(pk=pk)    
        posts.likes.add(request.user)
        return Response(status=200)

class UnlikePostView(APIView):
    """Unliking posts"""
    permission_classes = [permissions.IsAuthenticated]
    def put(self,request,pk):
        posts = Post.objects.get(pk=pk)    
        posts.likes.remove(request.user)
        return Response(status=200)

class CreateCommentPostView(generics.CreateAPIView):
    """Create comments for a specific post"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user,post_id=self.kwargs.get("post_id"))








