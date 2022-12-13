from django.contrib import admin
from .models import Todo,User,Tag
# Register your models here.

admin.site.register(Todo)
admin.site.register(User)
admin.site.register(Tag)