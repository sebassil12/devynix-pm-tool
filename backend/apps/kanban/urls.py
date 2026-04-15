from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KanbanBoardViewSet, KanbanColumnViewSet, KanbanCardViewSet

router = DefaultRouter()
router.register(r'boards', KanbanBoardViewSet, basename='board')
router.register(r'columns', KanbanColumnViewSet, basename='column')
router.register(r'cards', KanbanCardViewSet, basename='card')

urlpatterns = [
    path('', include(router.urls)),
]
