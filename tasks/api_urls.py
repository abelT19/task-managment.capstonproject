from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet  # Make sure this exists

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
