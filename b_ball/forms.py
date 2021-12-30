from django import forms
from django.forms import ModelForm
from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name',]
        player_name = forms.CharField()