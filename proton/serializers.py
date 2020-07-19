from rest_framework import serializers

from .models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'duration', 'last_edited', 'tasks')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'start_date','end_date', 'project')

