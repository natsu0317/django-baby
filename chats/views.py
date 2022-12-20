from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Chatroom,Chat
from .serializers import UserModelSerializer, ChatroomModelSerializer, ChatReadSerializer, ChatWriteSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class ChatView(APIView):
    def get(self, request, chatroom_id):
        comments=Chat.objects.filter(chatroom__id=chatroom_id)
        res_comments=[]
        for comment in comments:
            res_comment={
                'comment':comment.chat,
                'username':comment.created_by.username
            }
            res_comments.append(res_comment)
        return Response(res_comments)

#ある人が所属するchatroom一覧
class ChatroomView(APIView):
    def get(self,request,user_id):
        user=User.objects.get(id=user_id)
        rooms=user.user_chatroom.all()
        res_rooms=[]
        for room in rooms:
            res_room = {
                'room_name':room.chatroomname,
                'username':room.user.all().values('username'),
            }
            res_rooms.append(res_room)
        return Response(res_rooms)

class UserViewSet(ModelViewSet):
    serializer_class=UserModelSerializer
    queryset=User.objects.all()

class ChatroomViewSet(ModelViewSet):
    serializer_class=ChatroomModelSerializer
    queryset=Chatroom.objects.all()

class ChatViewSet(ModelViewSet):
    serializer_class=ChatReadSerializer
    queryset=Chat.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ChatReadSerializer
        else:
            return ChatWriteSerializer
