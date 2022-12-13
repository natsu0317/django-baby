from django.urls import path
from .views import todo_add, todo_delete,todo_list,TodoAddView,TodoDeleteView,get_tags_from_todo,get_todos_from_tag,get_todo_including_user_name,get_todos_from_user

app_name = 'todo'

urlpatterns = [
    path('',todo_list), #/todoにするとtodo_listに飛ぶ
    path('add/', todo_add),
    path('delete/<int:id>', todo_delete),
    path('todo-add/',TodoAddView.as_view()),
    path('todo-delete/<int:id>',TodoDeleteView.as_view()),
    path('get-tag/<int:id>',get_tags_from_todo),
    path('get-todos/<int:id>',get_todos_from_tag),
    path('get-todo-from-user/<int:id>',get_todo_including_user_name),
    path('get-todo/<int:id>',get_todos_from_user)
]
#tagのやつ微妙