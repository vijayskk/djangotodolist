from django.http import HttpResponse
from django.shortcuts import render
def todo(request):
    return render(request , "todo.html")