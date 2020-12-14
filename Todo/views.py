from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.


def view_tasks(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {'todos': todos, 'form': form}
    return render(request, 'Todo/index.html', context)


def add_task(request):
    # Create a form instance and populate it with data from the request
    form = TodoForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return redirect('view_tasks')

    # if the request does not have post data, a blank form will be rendered
    return render(request, 'Todo/index.html')


def delete_task(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == 'POST':
        todo.delete()
        return redirect('view_tasks')

    context = {'todo': todo}
    return render(request, 'Todo/delete.html', context)


def update_task(request, id):
    todo = Todo.objects.get(id=id)

    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        form.save()
        return redirect('view_tasks')

    context = {'form': form, 'todo': todo}
    return render(request, 'Todo/update.html', context)


def complete_task(request, id):
    todo = Todo.objects.get(id=id)

    todo.completed = True
    todo.save()
    return redirect('view_tasks')
