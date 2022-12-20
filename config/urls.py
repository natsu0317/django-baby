"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.http import JsonResponse


def hello_func(request):
    data = {
        "name": "Hibara"
    }
    return JsonResponse(data)

def cat_func(request):
    data = {
        "message": "Hello cat!"
    }
    return JsonResponse(data)

def animal_func(request, animal_name):
    data = {
        "message": "Hello" + animal_name + "!"
    }
    return JsonResponse(data)

def num_func(request, number):
    number += 1
    data = {
        "message": "Hello " + str(number) + "!"
    }
    return JsonResponse(data)

def search_func(request):
    search_query_param = request.GET.get("q")
    data = {
        "message": "Hello " + search_query_param + "!"
    }
    return JsonResponse(data)

def square_func(request, number):
    number = number ** 2
    data = {
        "data":str(number)
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello_func),
    path('cat' , cat_func),
    path('animal/<str:animal_name>', animal_func),
    path('num/<int:number>', num_func),
    path('search/', search_func),
    path('square/<int:number>', square_func),
    path('blog/', include('blog.urls')),
    path('todo/',include('todo.urls')),
    path('youtube/',include('youtube.urls')),
    path('chats/',include('chats.urls')),
]
