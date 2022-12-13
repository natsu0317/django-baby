from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo,User,Tag

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

class TodoAddView(APIView):
    def post(self,request):
        user_id=request.data["created_by"]
        user=User.objects.get(id=user_id)
        Todo.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            created_by=user,
            completed=request.data["completed"],
            duedate=None,
        )
        return Response(status=201)
        #status code があって201は成功したみたいなcode
        #postmanに  {"title":"buy chocolate",
                   # "description":"test",
                    #"completed":false}
                   # を打つ paramsの3こ左のbodyを押して一番右のtextをbodyに変更してrawに上のやつを変更して打つ


class TodoDeleteView(APIView):
    def delete(self,request,id):
        delete=Todo.objects.get(id=id)
        delete.delete()
        return Response(status=204)


def get_todos_from_tag(request,id):
    tag=Tag.objects.get(id=id)
    todos=tag.todos.all()
    return JsonResponse({
        "tags":[tag.name for tag in todos]
    })

def get_tags_from_todo(request,id):
    todo=Todo.objects.get(id=id)
    tags=todo.tags.all()
    return JsonResponse({
        "todos":[todo.name for todo in tags]
    })

#ResponseはAPIViewの中だけ
#普通のときはJsonResponseとかにする

def get_todo_including_user_name(request, id):
    todo = Todo.objects.get(id=id)
    return JsonResponse({
        "title": todo.title,
        "description": todo.description,
        "name": todo.created_by.name, #紐づいているUserのnameを取ってこれる！
        "completed": todo.completed,
        "duedate": todo.duedate
    })


def get_todos_from_user(request, id):
    user = User.objects.get(id=id)
    todos = user.fuga.all() #userに紐づいているTodoを取ってこれる！ (related_name='todos'と定義しているおかげ)
    return JsonResponse({
        "todos": [todo.title for todo in todos]
    })