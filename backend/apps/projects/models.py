from django.db import models
from apps.base.models import BaseModel
class Project(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return str(self.title)

class Node(BaseModel):
    class NodeType(models.TextChoices):
        KANBAN = 'kanban', 'Kanban'
        NOTEBOOK = 'notebook', 'Notebook'
        CANVAS = 'canvas', 'Canvas'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='nodes')
    parent_node = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=NodeType.choices)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'
        
    def __str__(self):
        return f"{self.title} ({self.type})"
