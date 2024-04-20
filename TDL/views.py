from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms  import TaskForm
from django.contrib.auth import authenticate, login
# Create your views here.



@login_required

@login_required
def index(request):
    activepage = "index"
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            
            if request.POST.get('complete'):
                task.mark_complete()
                
                
            return redirect('index')
                
            

    else:
        form = TaskForm()

    return render(
        request,
        'index.html',
        context={'tasks': tasks, 'form': form, 'activepage':activepage}
    )

    
def mark_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('tasks:index')

def delete_task(request,task_id):
    task = get_object_or_404(Task,pk = task_id)
    task.delete()
    return redirect('tasks:index')

def edit_task(request,task_id):
    task = get_object_or_404(Task, pk = task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')

    else :
        form = TaskForm(instance=task)
        
    return render(
        request,
        'edit_task.html',
        {'form':form , 'task':task}
        
        
        
    )


def formu(request):
    
    if request.method == 'POST':  
    
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            form.save()
            return HttpResponseRedirect('index')
        
    else:
        form = TaskForm()
    
    return render(
        
        request,
        'tasks_form.html',
        {'form':form}
        
        
    )

# def details(request,task_id):
#     details.Task.object.get()
#     return render(
#         request,
#         'details.html'
#         context={'Details':details}
#     )
    
def exit(request):
    logout(request)
    return redirect('login')



