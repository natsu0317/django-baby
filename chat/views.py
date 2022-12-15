from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Chatroom,Chat

class ChatView(APIView):
    def get(self, request, chatroom_id):
        chatrooms=Chatroom.objects.filter(chatroom_id=chatroom_id)
        res_comments=[]
        for chat in chatrooms:
            res_comment={
                'comment':Chat,
                'username':Chat.created_by.username
            }
            res_comments.append(res_comment)
        return (res_comments)

class ChatroomView(APIView):
    def get(self,request,user_id):
        user=User.objects.get(user_id=user_id)
        rooms=user.rooms.all()
        res_chatrooms=[]
        for room in rooms
        res_chatroom = {
            'room_name':Chatroom.chatroomname,
            'username':User.username,
            'chatroom':User.chatroom
        }
        res_chatrooms.append(res_chatroom)
        return(res_chatroom)