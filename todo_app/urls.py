from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('multi_delete/',views.multi_delete,name='multi_delete'),
]
