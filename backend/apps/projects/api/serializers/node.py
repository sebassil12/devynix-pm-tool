
from rest_framework import serializers
from apps.projects.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'title': instance['title'],
            'type': instance['type'],
            'created_at': instance['created_at'],
        }