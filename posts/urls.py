from django.urls import path
from .views import CreatePostView,UpdatePostView,DeletePostView,RepostView,LikePostView,UnlikePostView,CreateCommentPostView

urlpatterns = [
    path("",CreatePostView.as_view(),name="create-post"),
    path("<int:pk>/delete",DeletePostView.as_view(),name="delete-post"),
    path("<int:original_post_id>/repost",RepostView.as_view(),name="repost"),
    path("<int:pk>/edit",UpdatePostView.as_view(),name="edit-post"),
    path("<int:pk>/like",LikePostView.as_view(),name="like-post"),
    path("<int:pk>/unlike",UnlikePostView.as_view(),name="like-post"),
    path("<int:pos_id>/commments",CreateCommentPostView.as_view(),name="create-post"),


]