from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import TodoItem

def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")

def complete_task(request, uid):
    print(uid)
    return HttpResponse("OK")

def delete_task(request, uid):
    print(uid)
    return redirect("/tasks/list")



def tasks_list(request):
    all_tasks = TodoItem.objects.all()
    return render(
        request,
        'list.html',
        {'tasks': all_tasks}
    )