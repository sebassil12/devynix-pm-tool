from django.db import models
from apps.projects.models import Node
from apps.base.models import BaseModel
class Notebook(BaseModel):
    node = models.OneToOneField(Node, on_delete=models.CASCADE, related_name='notebook')
    content = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Notebook'
        verbose_name_plural = 'Notebooks'
    
    def __str__(self):
        return f"Notebook for {self.node.title}"
