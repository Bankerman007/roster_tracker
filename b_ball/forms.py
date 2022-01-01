from django import forms
from django.forms import ModelForm
from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name','player_email','player_cell']
        player_name = forms.CharField()
        player_email = forms.CharField()
        player_cell = forms.CharField()