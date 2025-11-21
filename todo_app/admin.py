from django.contrib import admin
from .models import Task, Note

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'due_date', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'created_at', 'due_date']
    search_fields = ['title', 'description']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    search_fields = ['title', 'content']
