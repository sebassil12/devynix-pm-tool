from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.kanban.models import KanbanColumn
from apps.kanban.api.serializers.kanban_column import KanbanColumnSerializer, KanbanColumnListSerializer

@api_view(['GET', 'POST'])
def kanban_column_api_view(request):

    if request.method == 'GET':
        kanban_columns = KanbanColumn.objects.all().values('id', 'board_id', 'title', 'position', 'created_at')
        kanban_column_serializer = KanbanColumnListSerializer(kanban_columns, many=True)
        return Response(kanban_column_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        kanban_column_serializer = KanbanColumnSerializer(data=request.data)
        if kanban_column_serializer.is_valid():
            kanban_column_serializer.save()
            return Response(kanban_column_serializer.data, status=status.HTTP_201_CREATED)
        return Response(kanban_column_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
