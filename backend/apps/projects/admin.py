from django.contrib import admin
from apps.projects.models import Node, Project
# Register your models here.

admin.site.register(Project)
admin.site.register(Node)