from django import forms

# project imports
from .models import Floor,Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['roomid']

        # TODO Add labels - class NameForm(forms.Form):
        # your_name = forms.CharField(label='Your name', max_length=100)
