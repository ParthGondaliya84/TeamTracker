from django.db import models
from apps.base.models import BaseModel
from apps.user.models import TeamUser
from apps.tasks.constant import Status


class Task(BaseModel):
    title = models.CharField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    assigned_by = models.ForeignKey(TeamUser, models.CASCADE, related_name='tasks_assigned_by')
    assigned_to = models.ForeignKey(TeamUser, models.CASCADE, related_name='tasks_assigned_to')
    deadline = models.DateTimeField(null=False, blank=False)
    status = models.CharField(
        choices=Status.choices(), default=Status.PENDING
    )

    def __str__(self):
        return f"{self.created_by} - {self.title}"
    

    class Meta:
        db_table = "task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']


class TaskComment(BaseModel):
    task = models.ForeignKey(Task, models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.created_by} - {self.comment[:50]}"


    class Meta:
        db_table = "task_comment"
        verbose_name = "Task comment"
        verbose_name_plural = "Task comments"
        ordering = ['-created_at']


class Notification(BaseModel):
    message = models.CharField(max_length=70)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.created_by} - {self.message}"
             

    class Meta:
        db_table = "notification"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-created_at']
