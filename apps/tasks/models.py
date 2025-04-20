from django.db import models
from apps.base.models import BaseModel
from apps.user.models import TeamUser
from apps.tasks.constant import Status


class Task(BaseModel):
    title = models.CharField()
    description = models.TextField()
    assigned_by = models.ForeignKey(TeamUser, models.CASCADE, related_name='tasks_assigned_by')
    assigned_to = models.ForeignKey(TeamUser, models.CASCADE, related_name='tasks_assigned_to')
    deadline = models.DateTimeField()
    status = models.CharField(
        choices=Status.choices(), default=Status.PENDING
    )

    def __str__(self):
        return f"{self.created_by} - {self.title}"


class TaskComment(BaseModel):
    task = models.ForeignKey(Task, models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.created_by} - {self.comment[:50]}"


class Notification(BaseModel):
    message = models.CharField(max_length=70)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.created_by} - {self.message}"
             
