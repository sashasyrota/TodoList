from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task


def index(request):
    task_list = Task.objects.all()

    context = {
        'task_list': task_list
    }

    return render(request, "todo/index.html", context=context)

class TaskListView(ListView):
    model = Task
    context_object_name = "task_list"
