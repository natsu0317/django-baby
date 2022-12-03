from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todo_add(request):
    return HttpResponse("todo追加しました")


def todo_delete(request):
    return HttpResponse("todo削除しました")