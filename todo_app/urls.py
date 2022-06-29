from django.urls import path, include
from todo_app import views
from rest_framework import routers
from  . views import TaskViewset


# router=routers.DefaultRouter()
router=routers.SimpleRouter()
router.register('task',TaskViewset)
router.register('completed_task',views.CompletedTaskviewset)
router.register('due_task',views.DueTaskViewset)
urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('multi_delete/<str:id_list_string>/',views.multi_delete,name='multi_delete'),
    path('edit_task_view/<int:id>/',views.edit_task_view,name='edit_task_view'),
    path('', views.task_view, name='task_view'),
    path('cbvtask/', views.TaskListView.as_view(), name='cbvtask'),
    path('taskapi/',include(router.urls))
]
