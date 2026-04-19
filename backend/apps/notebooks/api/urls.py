from django.urls import path
from apps.notebooks.api.views.notebook import notebook_api_view

urlpatterns = [
    ### Notebooks ###
    path('notebooks/', notebook_api_view, name='notebook_api'),
]