from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.models import TodoItem
from tasks.forms import AddTaskForm

def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")

def complete_task(request, uid):
    print(uid)
    return HttpResponse("OK")

def delete_task(request, uid):
    print(uid)
    return redirect("/tasks/list")

def task_create(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            desc = cd["description"]
            t = TodoItem(description=desc)
            t.save()
            return redirect("/tasks/list")
    else:
        form = AddTaskForm()
    return render(request, "tasks/create.html", {"form": form})

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