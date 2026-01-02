from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'status', 'due_date', 'completed_at']
    list_filter = ['status', 'priority', 'due_date', 'user']  # Filters in sidebar
    search_fields = ['title', 'description', 'user__username']
    ordering = ['due_date']  # Default ordering
