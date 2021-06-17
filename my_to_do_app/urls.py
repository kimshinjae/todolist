# my_to_do_app > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createTodo/', views.createTodo),
    path('deleteTodo/', views.deleteTodo)
]