from django.shortcuts import render,reverse

# add generic class views as needed, CRUD
from django.views.generic import (ListView,DetailView)

# project imports
from .models import Room


# Create your views here.
class RoomListView(ListView):
    model = Room

class RoomDetailView(DetailView):
    model = Room
