from rest_framework import viewsets
from .models import Notebook
from .serializers import NotebookSerializer

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
