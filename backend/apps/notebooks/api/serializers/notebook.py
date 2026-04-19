from rest_framework import serializers
from apps.notebooks.models import Notebook

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = '__all__'

class NotebookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'node': instance['node'],
            'content': instance['content'],
            'created_at': instance['created_at'],
        }