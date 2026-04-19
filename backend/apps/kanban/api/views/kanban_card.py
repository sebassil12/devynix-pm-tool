from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.kanban.models import KanbanCard
from apps.kanban.api.serializers.kanban_card import KanbanCardSerializer, KanbanCardListSerializer

@api_view(['GET', 'POST'])
def kanban_card_api_view(request):

    if request.method == 'GET':
        kanban_cards = KanbanCard.objects.all().values('id', 'column_id', 'title', 'description', 'priority', 'position', 'deadline', 'created_at')
        kanban_card_serializer = KanbanCardListSerializer(kanban_cards, many=True)
        return Response(kanban_card_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        kanban_card_serializer = KanbanCardSerializer(data=request.data)
        if kanban_card_serializer.is_valid():
            kanban_card_serializer.save()
            return Response(kanban_card_serializer.data, status=status.HTTP_201_CREATED)
        return Response(kanban_card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
