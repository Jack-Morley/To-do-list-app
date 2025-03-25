from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('index')

from django.views.decorators.http import require_POST

@require_POST
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')