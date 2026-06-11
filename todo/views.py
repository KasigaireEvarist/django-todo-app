from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('/')

    return render(request, 'todo/task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('/')

    return render(request, 'todo/task_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Show tasks + Add task
def task_list(request):

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Task.objects.create(title=title)

        return redirect('/')

    tasks = Task.objects.all()

    return render(request, 'todo/task_list.html', {'tasks': tasks})


# Delete task
def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect('/')


# Update task
def update_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':

        title = request.POST.get('title')

        if title:
            task.title = title
            task.save()

        return redirect('/')

    return render(request, 'todo/update_task.html', {'task': task})

def task_list(request):
    ...
