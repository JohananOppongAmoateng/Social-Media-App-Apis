from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
# Create your views here.
from .models import Group,GroupMember
from .serializers import GroupSerializer,GroupMemberSerializer
# Create your views here.


class CreateGroupView(generics.CreateAPIView):
    """Create Group"""
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()

    def perform_create(self,serializer):
        group = serializer.save(created_by=self.request.user)
        GroupMember.objects.create(group_id=group.id,member_id=group.created_by,admin=True)

class JoinGroupView(generics.CreateAPIView):
    """
    Class for joining group
    """
    
    serializer_class = GroupMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = GroupMember.objects.all()

    def perform_create(self,serializer):
        serializer.save(member_id=self.request.user,group_id=self.self.kwargs.get("pk"))


class LeaveGroupView(generics.DestroyAPIView):
    """
    Class for exiting group
    """
    serializer_class = GroupMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return GroupMember.objects.filter(member_id=self.request.user)

    

