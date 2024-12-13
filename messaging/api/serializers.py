from django.contrib.auth import get_user_model
from rest_framework import serializers

from messaging.models import Chat, Message

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['id', 'name', 'participants', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'text', 'created_at']
