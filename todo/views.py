from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo(request):
    todos = None
    is_authenticated = request.user.is_authenticated
    todos = Todo.objects.filter(user=request.user) if is_authenticated else None
    return render(
        request,
        "todo/todo.html",
        {"is_authenticated": is_authenticated, "todos": todos},
    )
