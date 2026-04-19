from rest_framework import serializers
from apps.kanban.models import KanbanCard

class KanbanCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanCard
        fields = '__all__'

class KanbanCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = KanbanCard
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'column_id': instance['column_id'],
            'title': instance['title'],
            'description': instance['description'],
            'priority': instance['priority'],
            'position': instance['position'],
            'deadline': instance['deadline'],
            'created_at': instance['created_at'],
        }
