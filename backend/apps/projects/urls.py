from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, NodeViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'nodes', NodeViewSet, basename='node')

urlpatterns = [
    path('', include(router.urls)),
]
