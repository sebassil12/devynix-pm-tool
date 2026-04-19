from rest_framework import serializers
from apps.kanban.models import KanbanColumn

class KanbanColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanColumn
        fields = '__all__'

class KanbanColumnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanColumn
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'board_id': instance['board_id'],
            'title': instance['title'],
            'position': instance['position'],
            'created_at': instance['created_at'],
        }
