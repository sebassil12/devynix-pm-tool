from rest_framework import serializers
from apps.kanban.models import KanbanBoard

class KanbanBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanBoard
        fields = '__all__'

class KanbanBoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanBoard
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'node_id': instance['node_id'],
            'config': instance['config'],
            'created_at': instance['created_at'],
        }
