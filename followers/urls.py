from django.urls import path
from .views import FollowUser,ListFollowersAndFollowing
urlpatterns = [
    path("follow",FollowUser.as_view(),name="follow"),
    path("",ListFollowersAndFollowing.as_view(),name="list-followers-and-following"),
]