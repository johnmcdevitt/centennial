from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# project specific imports
from .models import Card

# Create your views here.
class CardCreateView(generic.CreateView):
    model = Card
    def get_success_url(self):
        return reverse('backlog')



class CardListView(generic.ListView):
    model = Card
