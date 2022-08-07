from django.contrib import admin
from .models import Player, Player_full_text_list, TurnOff
# Register your models here.
admin.site.register(Player)
admin.site.register(Player_full_text_list)
admin.site.register(TurnOff)