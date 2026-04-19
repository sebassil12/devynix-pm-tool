from django.urls import path
from apps.projects.api.views.project import project_api_view

urlpatterns = [
    path('projects/', project_api_view, name='project_api'),
]