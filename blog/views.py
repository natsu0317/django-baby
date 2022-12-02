from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_list(request):
    return HttpResponse("初投稿です！")


def blog_like(request):
    return HttpResponse("いいねしました！")