from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskHistoryViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="tasks")
router.register(r'history', TaskHistoryViewSet, basename="history")

urlpatterns = [
    path('', include(router.urls)),
]
