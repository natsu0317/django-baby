from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    chatroom=models.ManyToManyField('Chatroom',related_name='chatroom_user', null=True, blank=True)

    def __str__(self):
        return self.username

class Chatroom(models.Model):
    chatroomname=models.CharField(max_length=100)
    user=models.ManyToManyField(User,related_name='user_chatroom')

    def __str__(self):
        return self.chatroomname

class Chat(models.Model):
    chat=models.TextField()
    chatroom=models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="chat")
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chat
