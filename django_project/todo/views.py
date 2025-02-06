from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            Todo.objects.create(name=name, description=description)
        return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    print("")
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(TOdo, id=todo_id)
    todo.delete()
    return redirect('todo_list')



