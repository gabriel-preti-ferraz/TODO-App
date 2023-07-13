from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def todo_list(request):
    todos = Todo.objects.all()

    if 'add-todo' in request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(user=request.user, title=title, description=description)

    if 'delete-todo' in request.POST:
        todo_id = request.POST.get('id')
        Todo.objects.filter(id=todo_id).delete()
        messages.add_message(request, constants.SUCCESS, 'Tarefa deletada.')

    contexto = {'todos':todos}
    return render(request, 'todo-list.html', contexto)

@login_required
def todo_view(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if 'delete-todo' in request.POST:
        todo.delete()
        messages.add_message(request, constants.SUCCESS, 'Tarefa deletada.')
        return redirect('todo-list')

    contexto = {'todo':todo}
    return render(request, 'todo.html', contexto)