from django.urls import path
from apps.projects.api.views.project import project_api_view
from apps.projects.api.views.node import node_api_view

urlpatterns = [
    ### Projects ###
    path('projects/', project_api_view, name='project_api'),

    ### Nodes ###
    path('nodes/', node_api_view, name='node_api'),
]