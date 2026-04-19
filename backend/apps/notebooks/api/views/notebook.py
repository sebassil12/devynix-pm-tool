from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.notebooks.models import Notebook
from apps.notebooks.api.serializers.notebook import NotebookListSerializer, NotebookSerializer

@api_view(['GET', 'POST'])
def notebook_api_view(request):
    if request.method == 'GET':
        notebooks = Notebook.objects.all().values('id', 'node', 'content', 'created_at')
        notebook_serializer = NotebookListSerializer(notebooks, many=True)
        return Response(notebook_serializer.data)

    elif request.method == 'POST':
        notebook_serializer = NotebookSerializer(data=request.data)
        if notebook_serializer.is_valid():
            notebook_serializer.save()
            return Response(notebook_serializer.data, status=status.HTTP_201_CREATED)
        return Response(notebook_serializer.errors, status=status.HTTP_400_BAD_REQUEST)