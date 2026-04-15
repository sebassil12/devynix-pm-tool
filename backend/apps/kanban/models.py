from django.db import models
from apps.projects.models import Node

class KanbanBoard(models.Model):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, related_name='kanban_board')
    config = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Board for {self.node.title}"

class KanbanColumn(models.Model):
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

class KanbanCard(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    column = models.ForeignKey(KanbanColumn, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    position = models.IntegerField(default=0)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title
