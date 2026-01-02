from django.urls import path
from .views import (
    task_list_view,
    update_task_view,
    delete_task_view,
    mark_complete_view,
    mark_incomplete_view,
)

urlpatterns = [
    path('', task_list_view, name='task-list'),
    path('update/<int:pk>/', update_task_view, name='update-task'),
    path('delete/<int:pk>/', delete_task_view, name='delete-task'),
    path('complete/<int:pk>/', mark_complete_view, name='mark-complete'),
    path('incomplete/<int:pk>/', mark_incomplete_view, name='mark-incomplete'),
]
