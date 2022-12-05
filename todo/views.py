from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Todo
from django.contrib.auth.models import User

me=User.objects.get(username='natsu0317')
# Create your views here.

def todo_list(request):
    tasks = Todo.objects.all()
    data ={
        "tasks": list(tasks.values())
    }
    return JsonResponse(data)

def todo_add(request):
    tasks = Todo.objects.create(author=me,title='Sample title',text='Test')
    data ={
        "tasks":list(tasks.values())
    }
    return JsonResponse(data)

def todo_delete(request,id):
    tasks = Todo.objects.delete