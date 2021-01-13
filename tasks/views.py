from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.utils import timezone

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.pub_date = timezone.now()
            new_task.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(instance=task)
    context = {'form': form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, "tasks/detail.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, "tasks/delete.html", context)




