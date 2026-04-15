from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Node(models.Model):
    class NodeType(models.TextChoices):
        KANBAN = 'kanban', 'Kanban'
        NOTEBOOK = 'notebook', 'Notebook'
        CANVAS = 'canvas', 'Canvas'

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='nodes')
    parent_node = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=NodeType.choices)
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type})"
