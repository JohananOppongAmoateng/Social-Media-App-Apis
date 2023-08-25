from django.urls import path
from .views import CreateGroupView,JoinGroupView,LeaveGroupView

urlpatterns = [
    path("",CreateGroupView.as_view(),name="create-group"),
    path("<int:pk>/join",JoinGroupView.as_view(),name="join-group"),
    path("<int:pk>/leave",LeaveGroupView.as_view(),name="leave-group")
    # path("",CreateGroupView.as_view(),name="create=group")
    # path("",CreateGroupView.as_view(),name="create=group")
    # path("",CreateGroupView.as_view(),name="create=group")

]