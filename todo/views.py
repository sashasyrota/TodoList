from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request):
    task_list = Task.objects.all()

    context = {"task_list": task_list}

    return render(request, "todo/index.html", context=context)


class TaskCompleteView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo:index"))


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_form.html"
    success_url = reverse_lazy("todo:index")


class TagsListView(ListView):
    model = Tag
    template_name = "todo/tags_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_confirm_form.html"
    success_url = reverse_lazy("todo:tags_list")
