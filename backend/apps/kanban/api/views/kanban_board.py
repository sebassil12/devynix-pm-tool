from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.kanban.models import KanbanBoard
from apps.kanban.api.serializers.kanban_board import KanbanBoardSerializer, KanbanBoardListSerializer

@api_view(['GET', 'POST'])
def kanban_board_api_view(request):

    if request.method == 'GET':
        kanban_boards = KanbanBoard.objects.all().values('id', 'node_id', 'config', 'created_at')
        kanban_board_serializer = KanbanBoardListSerializer(kanban_boards, many=True)
        return Response(kanban_board_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        kanban_board_serializer = KanbanBoardSerializer(data=request.data)
        if kanban_board_serializer.is_valid():
            kanban_board_serializer.save()
            return Response(kanban_board_serializer.data, status=status.HTTP_201_CREATED)
        return Response(kanban_board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
