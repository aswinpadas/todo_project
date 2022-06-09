from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('task',views.task_,name='task')
]
