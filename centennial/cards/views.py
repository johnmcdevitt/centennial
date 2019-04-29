from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect

# project specific imports
from .models import Card, CardType, CardTask
from .forms import CardTypeForm, CardForm

# Create your views here.
class CardCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    model = Card
    form_class = CardForm

    def get_context_data(self):
        type_details = CardType.objects.all()
        types = dict()
        for item in type_details:
            types[item] = dict(
                                icon=item.icon,
                                color=item.color,
                                name=item,
            )

        context = dict(form=CardForm(), types=types)

        return context

    # calling form_valid to allow saving of tasks to task model
    # with pk = card object
    def form_valid(self, form):
        self.object = form.save()

        print("card: ", self.object)
        print("task: ", self.request.POST.get('task0'))
        taskcount = 0
        for field in self.request.POST:
            if 'task' in field:
                print(field)
                taskcount += 1

        print("taskcount: ", taskcount)

        if taskcount > 0:
            tasks_to_save = {}
            for i in range(taskcount):
                print("in tasks to save loop")
                task_item = dict(
                    task=self.request.POST.get('task'+str(i)),
                    done=(self.request.POST.get('done'+str(i))=='true'),
                    card=self.object
                )
                tasks_to_save["task"+str(i)] = task_item
                print("tasks to save", tasks_to_save.keys())

            for k,v in tasks_to_save.items():
                print("in loop to create item", k)
                new_task = CardTask.objects.create(task=v['task'],
                                                  done=v['done'],
                                                  card=v['card'])
                new_task.save()
                print("task saving loop", k, new_task)

        return HttpResponseRedirect(self.get_success_url())



    def get_success_url(self):
        return reverse('kanban')

class CardUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "cards/card_form.html"
    model = Card
    form_class = CardForm
    success_message = "Success: Card was updated"
    success_url = reverse_lazy('kanban')

    # with pk = card object
    def form_valid(self, form):
        self.object = form.save()

        print("card: ", self.object)
        print("task: ", self.request.POST.get('task0'))
        taskcount = 0
        for field in self.request.POST:
            if 'task' in field:
                print(field)
                taskcount += 1

        print("taskcount: ", taskcount)

        if taskcount > 0:
            tasks_to_save = {}
            for i in range(taskcount):
                print("in tasks to save loop")
                task_item = dict(
                    task=self.request.POST.get('task' + str(i)),
                    done=(self.request.POST.get('done' + str(i)) == 'true'),
                    card=self.object
                )
                tasks_to_save["task" + str(i)] = task_item
                print("tasks to save", tasks_to_save.keys())

            for k, v in tasks_to_save.items():
                print("in loop to create item", k)
                new_task = CardTask.objects.create(task=v['task'],
                                                   done=v['done'],
                                                   card=v['card'])
                new_task.save()
                print("task saving loop", k, new_task)

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(CardUpdateView, self).get_context_data(**kwargs)
        type_details = CardType.objects.all()
        types = dict()
        for item in type_details:
            types[item] = dict(
                                icon=item.icon,
                                color=item.color,
                                name=item,
            )

        context['types'] = types

        return context



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
    success_url = reverse_lazy('card-types')

class CardTypeUpdateView(PassRequestMixin,SuccessMessageMixin,generic.UpdateView):
    template_name = "cards/update_cardtype.html"
    model = CardType
    form_class = CardTypeForm
    success_message = "Success: Card type was updated"
    success_url = reverse_lazy('card-types')


class CardTypeListView(generic.ListView):
    model = CardType
    context_object_name = 'cardtypes'

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

def update_task_api(request, pk):

    # TODO: no data validation here
    try:
        #get the object
        task = CardTask.objects.get(pk=pk)
        if ("done" in request.POST.keys()):
            task.done = request.POST["done"]
        task.save()
        response = dict(status=200,message="Updated task id "+str(pk))
        print("successful try")
    except CardTask.DoesNotExist as e:
        message="Task does not exist"
        response = dict(status=500,message=message)
        print("exception")
    except Exception as e:
                response = dict(status=500,message=str(TypeError(e)))
                print("exception")

    return JsonResponse(response)
