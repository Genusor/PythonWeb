from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from django.views.generic.detail import DetailView
from tasks.forms import AddTaskForm, TodoItemForm
from tasks.models import TodoItem

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")


def complete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse("OK")


def add_task(request):
    if request.method == "POST":
        desc = request.POST["description"]
        t = TodoItem(description=desc)
        t.save()
    return redirect(reverse("tasks:list"))


def delete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    return redirect(reverse("tasks:list"))


class TaskListView(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        u = self.request.user
        return u.task.all()

class TaskCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_task=form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect(reverse("tasks:list"))

        return render(request, "tasks/create.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, "tasks/create.html", {"form": form})
class TaskDetailsView(DetailView):
    model = TodoItem
    template_name = 'tasks/details.html'