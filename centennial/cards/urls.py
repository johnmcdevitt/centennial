from django.urls import path
from . import views

# app url patterns
urlpatterns = [
    path('',views.CardListView.as_view(),name='backlog'),
    path('create/',views.CardCreateView.as_view(),name='card-create'),
]
