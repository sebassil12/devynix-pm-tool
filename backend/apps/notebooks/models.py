from django.db import models
from apps.projects.models import Node

class Notebook(models.Model):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, related_name='notebook')
    content = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Notebook for {self.node.title}"
