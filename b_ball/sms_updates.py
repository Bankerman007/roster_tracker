import os
from twilio.rest import Client
from b_ball.models import Player, Player_full_text_list
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TextRegisteredPlayers, TextAllPlayers


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure




def sms_to_regist(form):
    message_to_send = form
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    this_weeks_players_dict = Player.objects.values('player_name', 'player_cell')
    this_weeks_list = []

    for ele in this_weeks_players_dict:
        for key, value in ele.items():
            v = value
            this_weeks_list.append(v)

    twl = {this_weeks_list[i]: this_weeks_list[i + 1] for i in range(0, len(this_weeks_list), 2)}
    twl_value = list(twl.values())
    tw_players = twl_value
    for p in tw_players:
        send_cell = p

        message = client.messages \
                        .create(
                             body= message_to_send,
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)

def sms_to_full_list(form):
    message_to_send = form
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    all_players_cells_dict = Player_full_text_list.objects.values('player_name_full_text','player_cell_full_text')
    all_players_list = []

    for ele in all_players_cells_dict:
        for key, value in ele.items():
            v = value
            all_players_list.append(v)

    apl = {all_players_list[i]: all_players_list[i + 1] for i in range(0, len(all_players_list), 2)}
    apl_value = list(apl.values())
    all_players = apl_value
    for p in all_players:
        send_cell = p

        message = client.messages \
                        .create(
                             body= message_to_send,
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)


        