from rest_framework import viewsets
from .models import KanbanBoard, KanbanColumn, KanbanCard
from .serializers import KanbanBoardSerializer, KanbanColumnSerializer, KanbanCardSerializer

class KanbanBoardViewSet(viewsets.ModelViewSet):
    queryset = KanbanBoard.objects.all()
    serializer_class = KanbanBoardSerializer

class KanbanColumnViewSet(viewsets.ModelViewSet):
    queryset = KanbanColumn.objects.all()
    serializer_class = KanbanColumnSerializer

class KanbanCardViewSet(viewsets.ModelViewSet):
    queryset = KanbanCard.objects.all()
    serializer_class = KanbanCardSerializer
