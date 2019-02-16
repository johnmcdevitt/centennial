from django.shortcuts import render
from django.urls import reverse
from django.views import generic

# project specific imports
from .models import Card

# Create your views here.
class CardCreateView(generic.CreateView):
    model = Card
    fields = ["title", "description","priority"]
    def get_success_url(self):
        return reverse('backlog')



class BacklogListView(generic.ListView):
    model = Card
    context_object_name = "backlog_cards"
    queryset = Card.objects.filter(status='100')

class TodoListView(generic.ListView):
    model = Card
    context_object_name = "todo_cards"
    queryset = Card.objects.filter(status='200')

class InprogressListView(generic.ListView):
    model = Card
    context_object_name = "inprogress_cards"
    queryset = Card.objects.filter(status='300')

class ReviewListView(generic.ListView):
    model = Card
    context_object_name = "review_cards"
    queryset = Card.objects.filter(status='400')

class DoneListView(generic.ListView):
    model = Card
    context_object_name = "done_cards"
    queryset = Card.objects.filter(status='500')

class KanbanBoardListView(generic.ListView):
    model = Card
    template_name = "cards/kanban_list.html"

    backlog_items = BacklogListView().queryset
    def get_context_data(self, *args, **kwargs):
        context = super(KanbanBoardListView, self).get_context_data(*args, **kwargs)
        context['backlog_cards'] = BacklogListView().queryset
        context['todo_cards'] = TodoListView().queryset
        context['inprogress_cards'] = InprogressListView().queryset
        context['review_cards'] = ReviewListView().queryset
        context['done_cards'] = DoneListView().queryset

        return context
