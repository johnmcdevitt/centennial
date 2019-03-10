from django.urls import path
from . import views

# app url patterns
urlpatterns = [
    # room patterns
    path('room/',views.RoomListView.as_view(),name='rooms'),
    path('room/<int:pk>',views.RoomDetailView.as_view(),name='room-detail'),
]
