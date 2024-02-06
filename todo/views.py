from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')
        
    context = {"todos":todos,"form":form}
    return render(request,'todo/list.html', context)

def updateTodo(request, pk):
    #Get the existing Todo item with the specified id
    todo = Todo.objects.get(id=pk)
    #Populate the form with the existing Todo item data
    form = TodoForm(instance=todo)
    if request.method == "POST":
        # Bind the form with the submitted POST data and the existing Todo item
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            #Redirect to the Todo list page after updating
            return redirect('/todo/')
    #Render the update_todo.html template with the form
    context = {"form": form, "todo": todo}
    return render(request,'todo/update_todo.html', context)

def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/todo/')
    context = {"item": item}
    return render(request,'todo/delete.html', context)