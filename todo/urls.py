from django.urls import path

from . import views

urlpatterns = [
    path("addTodo", views.addTodo),
    path("removeTodo", views.removeTodo),
    path("", views.todo),
]