from django.urls import path, include
from rest_framework import routers
from apps.tasks.views import TaskAPIView

router = routers.DefaultRouter()
router.register(r'assign-task', TaskAPIView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
