from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Blog

# Create your views here.

def blog_list(request):
    return HttpResponse("初投稿です！")


def blog_like(request):
    return HttpResponse("いいねしました！")

def post_list(request):
    tasks = Blog.objects.all()
    data ={
        "tasks":list(tasks.values())
    }
    return JsonResponse(data)

def post_get(request):
    tasks = Blog.objects.get(id=1)
    data={
        "tasks":list(tasks.values())  
    }
    return JsonResponse(data)