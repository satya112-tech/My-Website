from django.urls import path
from todo.views import *

urlpatterns = [
    path('',index,name="list"),
    path('update_todo/<str:pk>/',updateTodo,name="update_todo"),
    path('delete/<str:pk>/',deleteTodo,name="delete"),
]