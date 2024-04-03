from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
import json

def todo(request):
    f = open('todo/data.json')
    data = json.load(f)
    return render(request , "todo.html", {'todos': data["todos"]})

def addTodo(request):
    if request.method == "GET":
        f = open('todo/data.json')
        data = json.load(f)
        data["todos"].append({
            "id":str(uuid.uuid1()),
            "note":str(request.GET.get('note')),
            "completed":False
        })
        print(data["todos"]) 
        o = open('todo/data.json','w')
        json.dump(data,o,indent=6)
        o.close()
        f.close()

    return redirect('/')


def removeTodo(request):
    if request.method == "GET":
        f = open('todo/data.json')
        data = json.load(f)
        print(data["todos"]) 
        index = 0
        res = -1
        for i in data["todos"]:
            if i["id"] == request.GET.get('id'):
                res = index
            index += 1
        if res != -1:
            data["todos"].pop(res)
        o = open('todo/data.json','w')
        json.dump(data,o,indent=6)
        o.close()
        f.close()

    return redirect('/')

