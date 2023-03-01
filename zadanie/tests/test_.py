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
    return User.objects.create(username='TestUser', password='testpassword')


@pytest.fixture
@freeze_time("2022-02-22 12:00:00")
def task(user):
    task = Task.objects.create(
        name = 'TestTask',
        description = "TestDescription",
        status = 'In Progress',
        assigned_user = user
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


#update


@freeze_time("2022-02-22 13:00:00")
@pytest.mark.django_db
def test_Task_update(user, task):

    data = {
        'name': 'Updated Task',
        'description': 'This is an updated test task',
        'status': 'Resolved',
        'assigned_user': None
    }

    client = APIClient()
    url = reverse('tasks-detail', args=[task.id])
    client.force_authenticate(user=user)
    response = client.patch(url, data, format='json')

    assert response.status_code == 200


    assert response.json() == {
        'id': task.id,
        'name': 'Updated Task',
        'description': 'This is an updated test task',
        'status': 'Resolved',
        'assigned_user': None,
        'created_at': "2022-02-22 13:00:00"
    }

    task.refresh_from_db()

    expected_history_data = {
        'id' : ANY,
        'task_id': task.id,
        'name': 'TestTask',
        'description': 'TestDescription',
        'status': 'In Progress',
        'assigned_user_id': user.id,
        'valid_from': datetime.datetime(2022, 2, 22, 12, 0, tzinfo=datetime.timezone.utc),
        'valid_until': timezone.now()
    }

    assert TaskHistory.objects.filter(task=task).count() == 1
    assert TaskHistory.objects.filter(task=task).values().first() == expected_history_data

    expected_task_data = {
        'id': task.id,
        'name': 'Updated Task',
        'description': 'This is an updated test task',
        'status': 'Resolved',
        'assigned_user_id': None,
        'created_at': timezone.now()
    }
    task = Task.objects.values().get(id=response.json()["id"])
    assert task == expected_task_data


    
