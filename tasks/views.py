from django.shortcuts import render , redirect
from django.http import HttpResponse
from tasks.models import Task
from  tasks.forms import *
# Create your views here.
def index(request):

    tasks = Task.objects.all()
   
    form = TaskForm()
    # validation
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'tasks':tasks , 'forms':form }
    return render(request , 'tasks/list.html',context)


def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm( request.POST , instance=task)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form':form}
    return render(request , 'tasks/update_task.html' , context)


def deleteTask(request,pk):
    item = Task.objects.get(id = pk)
    context = {'item':item}

    if request.method =="POST":
        item.delete()
        return redirect("/")
     
    return render(request , 'tasks/delete_task.html' , context)
