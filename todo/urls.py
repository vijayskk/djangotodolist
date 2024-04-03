from django.urls import path

from . import views

urlpatterns = [
    path("addTodo", views.addTodo),
    path("removeTodo", views.removeTodo),
    path("checkTodo", views.checkTodo),
    path("", views.todo),
]