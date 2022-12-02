from django.urls import path
from .views import todo_add, todo_delete

app_name = 'todo'

urlpatterns = [
    path('add', todo_add),
    path('delete', todo_delete)
]