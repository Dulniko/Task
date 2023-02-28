import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient
from tasks.models import Task, TaskHistory
from tasks.serializers import TaskSerializer, TaskHistorySerializer
from unittest.mock import ANY
from freezegun import freeze_time
import datetime
#fixture


@pytest.fixture
def user():
    return User.objects.create(username='TestUser')

@pytest.fixture
def task(user):
    task = Task.objects.create(
        name = 'TestTask',
        description = "TestDescription",
        status = 'In Progress',
        assigned_user = user.id
    )
    return task


#creation

@freeze_time("2022-02-22 12:00:00")
@pytest.mark.django_db
def test_Task_creation(user):
    
    data = {
        'name': 'Test Task',
        'description': 'This is a test task',
        'status': 'In Progress',
        'assigned_user': user.id
    }

    client = APIClient()
    url = reverse('tasks-list')
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.json() == {
        'id' : ANY,
        'name': 'Test Task',
        'description': 'This is a test task',
        'status': 'In Progress',
        'assigned_user': user.id,
        'created_at' : "2022-02-22 12:00:00"
    }

    task = Task.objects.values().get(id=response.json()["id"])

    expected_data = {
        'id' : ANY,
        'name': 'Test Task',
        'description': 'This is a test task',
        'status': 'In Progress',
        'assigned_user_id': user.id,
        'created_at' : timezone.now()
    }
        
    assert task == expected_data