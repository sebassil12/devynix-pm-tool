from django.contrib import admin
from apps.kanban.models import KanbanBoard, KanbanColumn, KanbanCard
# Register your models here.
admin.site.register(KanbanBoard)
admin.site.register(KanbanColumn)
admin.site.register(KanbanCard)