from django.db import models
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'chat'

router = DefaultRouter()
router.register(r'user',views.UserViewSet,basename='user')#chats/user/
router.register(r'chatroom',views.ChatroomViewSet,basename='chatroom')
router.register(r'chat',views.ChatViewSet,basename='chat')
urlpatterns=router.urls

urlpatterns += [
    path('<int:chatroom_id>/comments/', views.ChatView.as_view()),
    path('<int:user_id>/chatrooms/',views.ChatroomView.as_view()),
]