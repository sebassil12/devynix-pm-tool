from django.db import models
from apps.projects.models import Node
from apps.base.models import BaseModel

class KanbanBoard(BaseModel):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, related_name='kanban_board')
    config = models.JSONField(default=dict, blank=True)
    class Meta:
        verbose_name = 'Kanban Board'
        verbose_name_plural = 'Kanban Boards'

    def __str__(self):
        return f"Board for {self.node.title}"

class KanbanColumn(BaseModel):
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'Kanban Column'
        verbose_name_plural = 'Kanban Columns'

    def __str__(self):
        return self.title

class KanbanCard(BaseModel):
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

    class Meta:
        ordering = ['position']
        verbose_name = 'Kanban Card'
        verbose_name_plural = 'Kanban Cards'

    def __str__(self):
        return self.title