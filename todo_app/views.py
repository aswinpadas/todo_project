from django.shortcuts import render

# Create your views here.
from todo_app.models import Task


def task(req):
    if req.method=='POST':
        name=req.POST.get('name')
        priority=req.POST.get('priority')
        obj_task=Task(name=name,priority=priority)
        obj_task.save()
    return  render(req,"task.html",{})
def task_view(req):
    obj_task=Task.objects.all()
    # if req.method == 'POST':
    #     name=req.POST.get('name')
    #     priority=req.POST.get('priority')
    #     obj_task=Task(name=name,priority=priority)
    #     obj_task.save()
    return render(req,"task_view.html",{'obj_task':obj_task})
