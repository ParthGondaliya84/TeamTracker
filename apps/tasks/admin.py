from django.contrib import admin
from apps.tasks.models import Task, TaskComment, Notification


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'assigned_by', 'assigned_to', 'deadline', 'status'
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment)
admin.site.register(Notification)
