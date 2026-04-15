from rest_framework import serializers
from .models import Project, Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'
