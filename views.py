from rest_framework import generics # type: ignore
from rest_framework import permissions # type: ignore
from .models import CustomUser, Friendship
from .seralize import UserSerializer, FriendshipSerializer

class UserSearchAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        return CustomUser.objects.filter(email__icontains=keyword) | CustomUser.objects.filter(username__icontains=keyword)

class FriendshipRequestAPIView(generics.CreateAPIView):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)
