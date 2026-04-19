from rest_framework import serializers
from apps.projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
    
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'title': instance['title'],
            'description': instance['description'],
            'created_at': instance['created_at'],
        }