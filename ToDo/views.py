from django.shortcuts import render,redirect
from django.utils import timezone
from .models import TodoDB
# Create your views here.
def index(request):
    todoitem=TodoDB.objects.all().order_by("-date")
    return render(request,'ToDo/index.html',{"todo_item":todoitem})


def add_todo(request):
    if request.method=='POST':
        content=request.POST.get('todo')
        added_date=timezone.now()
        if content!='':
            TodoDB.objects.create(date=added_date,text=content)
           # TodoDB.save()
            print(added_date)
            print(content)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def del_todo(request,todoid):
    print(todoid)
    TodoDB.objects.get(id=todoid).delete()
    return redirect('/')