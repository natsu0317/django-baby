
from rest_framework import serializers
from .models import User,Chatroom,Chat

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

class ChatroomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chatroom
        fields=['chatroomname']

class ChatReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'

class ChatWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'