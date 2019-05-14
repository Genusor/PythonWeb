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

def task_create(request):
    return render(
        request,
        'tasks/create.html',
    )

def tasks_list(request):
    all_tasks = TodoItem.objects.all()
    return render(
        request,
        'tasks/list.html',
        {'tasks': all_tasks}
    )

def add_task(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = TodoItem(description=desc)
        t.save()
    return redirect("/tasks/list")