from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.models import Task


# def task(req):
#     if req.method=='POST':
#         name=req.POST.get('name')
#         priority=req.POST.get('priority')
#         obj_task=Task(name=name,priority=priority)
#         obj_task.save()
#     return  render(req,"task.html",{})
def task_view(req):
    if req.method == 'POST':
        print('request is', req.POST)
        name = req.POST.get('name')
        priority = req.POST.get('priority')
        obj_task_1 = Task(name=name, priority=priority)
        obj_task_1.save()
        return redirect('/')
        # req.POST.reset()
    obj_task_2 = Task.objects.all()
    return render(req, "task_view.html", {'obj_task': obj_task_2})

def edit_task_view(req,id):
    if req.method == 'POST':
        obj_task = Task.objects.get(id=id)
        name = req.POST.get('name')
        priority = req.POST.get('priority')
        obj_task.setTask(name,priority)
        obj_task.save()
        return redirect('/')
        # req.POST.reset()
    obj_task_2 = Task.objects.get(id=id)
    return render(req, "edit_task_view.html", {'result': obj_task_2})


def delete(req, id):
    obj_task = Task.objects.get(id=id)
    if req.method == 'POST':
        obj_task.delete()
        return redirect('/')
    return render(req, "delete.html", {'obj_task': obj_task})


def multi_delete(req, id_list_string):
    print('****************************************')
    if req.method == 'GET':
        id_list = id_list_string.split(',');
        print(id_list)
        for eid in id_list:
            obj_task = Task.objects.get(id=eid)
            obj_task.delete()
        return redirect('/')
    else:
        return render(req, "multi_delete.html")
