from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.projects.models import Project
from apps.projects.api.serializers.project import ProjectSerializer, ProjectListSerializer

@api_view(['GET', 'POST'])
def project_api_view(request):

    if request.method == 'GET':
        projects = Project.objects.all().values('id', 'title', 'description', 'created_at')
        project_serializer = ProjectListSerializer(projects, many=True)
        return Response(project_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        project_serializer = ProjectSerializer(data=request.data)
        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_201_CREATED)
        return Response(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)