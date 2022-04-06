from django.http import request
from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('tasks/', core.views.Tasks.as_view(), name='task_list'),
    path('tasks/<int:pk>/', core.views.TaskDetail.as_view(), name='task_detail'),
    path('tasks/create/', core.views.TaskCreate.as_view(), name='task_create'),
    path('tasks/<int:pk>/close', core.views.TaskClose, name='task_close'),
    path('tasks/<int:pk>/update', core.views.TaskUpdate.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete', core.views.TaskDelete.as_view(), name='task_delete'),
]
