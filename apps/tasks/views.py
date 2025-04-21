from apps.base.views import BaseViewSet
from rest_framework import viewsets
from apps.tasks.models import Task, TaskComment, Notification
from apps.tasks.serializers import TaskSerializer
from django.db.models import Q

class TaskAPIView(BaseViewSet, viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(
            Q(created_by=user) |
            Q(assigned_by=user) |
            Q(assigned_to=user)
        ).distinct()
        return queryset
