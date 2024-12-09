from django.shortcuts import render,redirect
from .models import task

def task_list(request):
        tasks = task.objects.all()
        return render(request, 'tasks/task_list.html',{'tasks':tasks})

def add_task(request):
        if request.method == 'POST':
                title = request.POST.get('title')
                if title:
                        task.objects.create(title = title)
                return redirect('task_list')
        return render(request, 'tasks/task_add.html')