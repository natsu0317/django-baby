from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

me=User.objects.get(username='natsu0317')
# Create your views here.

def todo_list(request):
    tasks = Todo.objects.all()
    data ={
        "tasks": list(tasks.values())
    }
    return JsonResponse(data)

def todo_add(request):
    tasks = Todo.objects.create(title='Sample title',description='Test',completed=False,duedate=auto_now_add)
    data ={
        "tasks":list(tasks.values())
    }
    return JsonResponse(data)

def todo_delete(request,id):
    tasks = Todo.objects.get(id=id)
    tasks.delete()
    data ={
        "tasks":list(tasks.values())
    }
    return JsonResponse(data)

class todo_add_view(APIView):
    def post(self,request):
        Todo.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            completed=request.data["completed"],
            duedate=None,
        )
        return Response(status=201)
        #status code があって201は成功したみたいなcode


class todo_delete_view(APIView):
    def delete(self,request,id):
        delete=Todo.objects.get(id=id)
        delete.delete()
        return Response(status=204)