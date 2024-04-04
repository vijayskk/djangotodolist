from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
import json
import time
from . import db
reloadit = False

def reload(request):
    return redirect('/')
def todo(request):
    try:
        data = db.db.todos.find()
    except Exception as e:
        print(e)
    finally:
        return render(request , "todo.html", {'todos': data})

def addTodo(request):
    if request.method == "GET":
            id = str(uuid.uuid1())
            try:  
                print("Working")         
                db.db.todos.insert_one({
                    "_id":id,
                    "id":id,
                    "note":str(request.GET.get('note')),
                    "completed":False
                })
            except Exception as e:
                print(e)
            finally:
                reload(request)
                return redirect('/')



async def removeTodo(request):
    if request.method == "GET":
        print(request.GET.get('id'))
        try:
            db.db.todos.delete_one({"_id":request.GET.get('id')})
            await time.sleep(1)
        except Exception as e:
            print(e)
        finally:   
            reload(request)
            return redirect('/')


async def checkTodo(request):
    if request.method == "GET":
        print(request.GET.get('id'))
        try:
            db.db.todos.update_one({"_id":request.GET.get('id')},{"$set": {"completed": True}})
            await time.sleep(1)
        except Exception as e:
            print(e)
        finally:  
            reload(request) 
            return redirect('/')

