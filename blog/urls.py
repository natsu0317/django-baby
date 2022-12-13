from django.urls import path
from .views import blog_list, blog_like,post_list,post_get

app_name = 'blog'


urlpatterns = [
    path('',post_list),
    path('get/<int:id>', post_get),
    path('list/', blog_list),
    path('like/', blog_like)
]