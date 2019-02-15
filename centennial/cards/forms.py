from django import forms
# from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _

# project specific imports
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
