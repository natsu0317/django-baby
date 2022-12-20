from django.contrib import admin
from .models import User,Chatroom,Chat
# Register your models here.

admin.site.register(User)
admin.site.register(Chatroom)
admin.site.register(Chat)