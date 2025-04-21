from rest_framework import serializers
from apps.base.serializers import BaseSerialzers
from apps.user.models import TeamUser
from apps.tasks.models import Task, TaskComment, Notification
from apps.tasks.constant import Status
from apps.user.choices import UserRole


class TeamuserSerializer(BaseSerialzers):

    class Meta:
        model = TeamUser
        fields = ["id", "email", "first_name", "last_name"]


class TaskSerializer(BaseSerialzers):
    assigned_by = serializers.PrimaryKeyRelatedField(
        queryset=TeamUser.objects.filter(user_role=UserRole.LEADER),
        many=True,
        required=False,
        write_only=True
    )
    assigned_by_detail = TeamuserSerializer(
        source = 'assigned_by',
        many=True,
        read_only=True
    )
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=TeamUser.objects.filter(user_role=UserRole.EMPLOYEE),
        many=True,
        required=False,
        write_only=True
    )
    assigned_to_detail = TeamuserSerializer(
        source = 'assigned_to',
        many=True,
        read_only=True
    )

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "assigned_by", "assigned_by_detail",
            "assigned_to", "assigned_to_detail", "deadline", "status"
        ]

    def validate(self, data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            if request.user.user_role != UserRole.LEADER:
                raise serializers.ValidationError("Only Leaders can assign tasks.")
            data['assigned_by'] = [request.user]
        return super().validate(data)

