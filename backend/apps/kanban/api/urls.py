from django.urls import path
from apps.kanban.api.views.kanban_board import kanban_board_api_view
from apps.kanban.api.views.kanban_column import kanban_column_api_view
from apps.kanban.api.views.kanban_card import kanban_card_api_view

urlpatterns = [
    ### Kanban Boards ###
    path('boards/', kanban_board_api_view, name='kanban_board_api'),

    ### Kanban Columns ###
    path('columns/', kanban_column_api_view, name='kanban_column_api'),

    ### Kanban Cards ###
    path('cards/', kanban_card_api_view, name='kanban_card_api'),
]
