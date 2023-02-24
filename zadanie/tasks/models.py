from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status_choices = [
        ('New', 'Nowy'),
        ('In Progress', 'W toku'),
        ('Resolved', 'Rozwiązany')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='New')
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)