from rest_framework import serializers
from .models import KanbanBoard, KanbanColumn, KanbanCard

class KanbanCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanCard
        fields = '__all__'

class KanbanColumnSerializer(serializers.ModelSerializer):
    cards = KanbanCardSerializer(many=True, read_only=True)
    class Meta:
        model = KanbanColumn
        fields = '__all__'

class KanbanBoardSerializer(serializers.ModelSerializer):
    columns = KanbanColumnSerializer(many=True, read_only=True)
    class Meta:
        model = KanbanBoard
        fields = '__all__'
