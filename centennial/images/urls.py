from django.urls import path
from . import views

# app url patterns
urlpatterns = [
    path('',views.ImageListView.as_view(),name='images'),
    path('create/',views.ImageCreateView,name='image-create'),
]
