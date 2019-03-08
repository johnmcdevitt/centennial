from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse

# project specific imports
from .models import Card, CardType
from .forms import CardTypeForm, CardForm

# Create your views here.
class CardCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "cards/card_form.html"
    model = Card
    form_class = CardForm
    success_url = reverse_lazy("kanban")


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

    queryset = Card.objects.all().order_by('order')

class CardTypeCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "cards/create_cardtype.html"
    form_class = CardTypeForm
    success_message = "Success: Card type was created"
    success_url = reverse_lazy('kanban')

def update_card_api(request, pk):

    # TODO: no data validation here
    try:
        #get the object
        card = Card.objects.get(pk=pk)
        if ("cardstatus" in request.POST.keys()):
            card.status = request.POST["cardstatus"]
        if ("order" in request.POST.keys()):
            card.order = request.POST["order"]
        card.save()
        response = dict(status=200,message="Updated card id "+str(pk))
        print("successful try")
    except Card.DoesNotExist as e:
        message="Card does not exist"
        response = dict(status=500,message=message)
        print("exception")
    except Exception as e:
                response = dict(status=500,message=str(TypeError(e)))
                print("exception")

    return JsonResponse(response)
