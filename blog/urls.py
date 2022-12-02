from django.urls import path
from .views import blog_list, blog_like

app_name = 'blog'


urlpatterns = [
    path('list', blog_list),
    path('like', blog_like)
]