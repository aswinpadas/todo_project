from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .serializers import TaskSerializers
from .models import Task
# Create your views here.
from django.views.generic import ListView

from rest_framework import viewsets


# def task(req):
#     if req.method=='POST':
#         name=req.POST.get('name')
#         priority=req.POST.get('priority')
#         obj_task=Task(name=name,priority=priority)
#         obj_task.save()
#     return  render(req,"task.html",{})

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date')
    serializer_class = TaskSerializers


class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date').filter(completed=False)
    serializer_class = TaskSerializers

class CompletedTaskviewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date').filter(completed=True)
    serializer_class = TaskSerializers


class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj_task'


def task_view(req):
    if req.method == 'POST':
        print('request is', req.POST)
        name = req.POST.get('name')
        priority = req.POST.get('priority')
        date = req.POST.get('date')
        obj_task_1 = Task(name=name, priority=priority, date=date)
        obj_task_1.save()
        return redirect('/')
        # req.POST.reset()
    obj_task_2 = Task.objects.all()
    taskname = ''
    taskpriority = ''
    title = 'Add task'
    button_name = 'Submit'
    return render(req, "task_view.html",
                  {'obj_task': obj_task_2, 'obj_taskname': taskname, 'obj_taskpriority': taskpriority, 'title': title,
                   'button_name': button_name})


def edit_task_view(req, id):
    obj_task_2 = Task.objects.all()
    obj_task_3 = Task.objects.get(id=id)
    taskname = obj_task_3.name
    taskpriority = obj_task_3.priority
    date = obj_task_3.date
    title = 'Edit Task'
    if req.method == 'POST':
        obj_task = Task.objects.get(id=id)
        # print('request is', req.POST)
        obj_task = Task.objects.get(id=id)
        name = req.POST.get('name')
        priority = req.POST.get('priority')
        date = req.POST.get('date')
        obj_task.setTask(name, priority, date)
        obj_task.save()
        return redirect('/')
        # req.POST.reset()
    button_name = 'Update'

    return render(req, "task_view.html",
                  {'obj_task': obj_task_2, 'obj_taskname': taskname, 'obj_taskpriority': taskpriority, 'date': date,
                   'title': title, 'button_name': button_name})

    # if req.method == 'POST':
    #     obj_task = Task.objects.get(id=id)
    #     name = req.POST.get('name')
    #     priority = req.POST.get('priority')
    #     date = req.POST.get('date')
    #     obj_task.setTask(name,priority,date)
    #     obj_task.save()
    #     return redirect('/')
    #     # req.POST.reset()
    # obj_task_2 = Task.objects.get(id=id)
    # return render(req, "edit_task_view.html", {'result': obj_task_2})


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
