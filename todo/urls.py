from django.urls import path
from .views import todo_add, todo_delete,todo_list

app_name = 'todo'

urlpatterns = [
    path('',todo_list), #/todoにするとtodo_listに飛ぶ
    path('add', todo_add),
    path('delete', todo_delete),
]