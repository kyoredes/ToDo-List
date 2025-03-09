from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ("id", "name", "description", "created_at", "complete", "tags", "user")
        extra_kwargs = {
            "name": {"required": True},
            "description": {"required": False},
        }
