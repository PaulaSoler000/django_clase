from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


""" @require_POST
def add(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    if title:
        task = Task(title=title, description=description)
        task.save()
        messages.success(request, 'Tarea añadida con éxito.')
    else:
        messages.error(request, 'El título de la tarea es obligatorio.')
    
    return redirect(index) """

def add(request):
    task = Task.objects.create()
    task.title = request.POST.get('title')
    task.description = request.POST.get('description')
    #task.completed = request.POST.get('completed')
    task.save()
    return redirect(index)

def create_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = TaskForm()
        return render(request, 'create_form.html', {'form': form})
    
    