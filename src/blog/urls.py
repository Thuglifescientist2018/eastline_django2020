from django.urls import path
from .views import blog_home, blog_list, blog_create, blog_render, blog_update, blog_delete

urlpatterns = [
    path("", blog_home),
    path("list", blog_list),
    path("create", blog_create),
    path("<str:slug>", blog_render),
    path("<str:slug>/update", blog_update),
    path("<str:slug>/delete", blog_delete)
    
]