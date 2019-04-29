from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _

# project specific imports
from .models import Card, CardType, CardTask

class CardForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['status','order']

class CardTypeForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = CardType
        fields = ['cardtype', 'color', 'icon']


class CardTaskForm(forms.ModelForm):
    class Meta:
        model = CardTask
        exclude = ["card",]