from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task, TaskHistory
from .serializers import TaskSerializer, TaskHistorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name', 'description', 'status', 'assigned_user']
    filterset_fields = ['assigned_user', 'status'] 

class TaskHistoryViewSet(viewsets.ModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = TaskHistorySerializer


    

