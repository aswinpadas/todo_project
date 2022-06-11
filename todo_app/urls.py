from django.urls import path
from todo_app import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('multi_delete/<str:id_list_string>/',views.multi_delete,name='multi_delete'),
    path('edit_task_view/<int:id>/',views.edit_task_view,name='edit_task_view'),
    path('', views.task_view, name='task_view')
]
