from django.urls import path
from .views import todo_add, todo_delete,todo_list,todo_add_view,todo_delete_view

app_name = 'todo'

urlpatterns = [
    path('',todo_list), #/todoにするとtodo_listに飛ぶ
    path('add/', todo_add),
    path('delete/<int:id>', todo_delete),
    path('todo-add/',todo_add_view.as_view()),
    path('todo-delete/<int:id>',todo_delete_view.as_view()),
]