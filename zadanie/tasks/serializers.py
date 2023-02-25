from rest_framework import serializers
from .models import Task, TaskHistory

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'assigned_user', 'created_at']

class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = ['id', 'task' ,'name', 'description', 'status', 'assigned_user', 'valid_from', 'valid_until']
        read_only_fields = fields
    
