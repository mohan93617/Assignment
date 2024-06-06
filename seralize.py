from rest_framework import serializers # type: ignore
from .models import CustomUser, Friendship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['requester', 'receiver', 'status']

