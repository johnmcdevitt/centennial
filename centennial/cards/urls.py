from django.urls import path
from . import views

# app url patterns
urlpatterns = [
    # TODO: path handle to patterns for backlog
    path(r'',views.KanbanBoardListView.as_view(),name='kanban'),
    path('backlog/',views.BacklogListView.as_view(),name='backlog'),
    path('to-do/',views.TodoListView.as_view(),name='to-do'),
    path('in-progress/',views.InprogressListView.as_view(),name='in-progress'),
    path('review/',views.ReviewListView.as_view(),name='review'),
    path('done/',views.DoneListView.as_view(),name='done'),
    path('kanban/',views.KanbanBoardListView.as_view(),name='kanban'),
    path('create/',views.CardCreateView.as_view(),name='create-card'),
    path('ajax/<int:pk>/edit/',views.update_card_api,name='update_card_api'),
    path('create-type/',views.CardTypeCreateView.as_view(),name='create-type'),
    path('types/',views.CardTypeListView.as_view(),name='card-types'),
    path('<int:pk>/edit/',views.CardTypeUpdateView.as_view(),name='update-type'),
]
