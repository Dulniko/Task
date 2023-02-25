from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework.response import Response
from .models import Task, TaskHistory
from .serializers import TaskSerializer, TaskHistorySerializer
import datetime

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name', 'description', 'status', 'assigned_user']
    filterset_fields = ['assigned_user', 'status'] 

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        TaskHistory.objects.create(
                task=instance,
                name=instance.name,
                description=instance.description,
                status=instance.status,
                assigned_user=instance.assigned_user,
                valid_from=instance.created_at,
            )

        self.perform_update(serializer)

        return Response(serializer.data)


class TaskHistoryFilter(FilterSet):
    task = NumberFilter(field_name='task__id')
    
    class Meta:
        model = TaskHistory
        fields = {
        'task': ['exact'],
        'valid_from': ['lte'],
        'valid_until': ['gte'],
    }


class TaskHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = TaskHistorySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskHistoryFilter