from django import forms
# from .models import Floor,Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# TODO custom registration forms


# profile form
class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'password', # TODO better display
                 ]
