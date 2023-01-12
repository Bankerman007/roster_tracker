from django import forms
from django.forms import ModelForm
from .models import Player, TurnOff, Player_full_text_list


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name','player_cell']
        player_name = forms.CharField()
        player_email = forms.CharField()
        player_cell = forms.CharField()

class EditPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name','player_cell']
        player_name = forms.CharField()
        player_cell = forms.CharField()

class AllPlayersForm(ModelForm):
    class Meta:
        model = Player_full_text_list
        fields = ['player_name_full_text','player_cell_full_text']
        player_name_full_text = forms.CharField()
        player_cell_full_text = forms.CharField()
        

class TextRegisteredPlayers(forms.Form):
    message = forms.CharField()
    
class TextAllPlayers(forms.Form):
    message = forms.CharField()

class TurnOnOff(ModelForm):
    class Meta:
        model = TurnOff
        fields= ['flag','on_off',]
        flag = forms.CharField()
        on_off = forms.BooleanField()
    
        
        