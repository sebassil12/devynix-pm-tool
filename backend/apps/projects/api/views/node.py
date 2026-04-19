
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.projects.models import Node
from apps.projects.api.serializers.node import NodeSerializer

@api_view(['GET', 'POST'])
def node_api_view(request):

    if request.method == 'GET':
        nodes = Node.objects.all().values('id', 'title', 'type', 'created_at')
        node_serializer = NodeSerializer(nodes, many=True)
        return Response(node_serializer.data)

    elif request.method == 'POST':
        node_serializer = NodeSerializer(data=request.data)
        if node_serializer.is_valid():
            node_serializer.save()
            return Response(node_serializer.data, status=status.HTTP_201_CREATED)
        return Response(node_serializer.errors, status=status.HTTP_400_BAD_REQUEST)