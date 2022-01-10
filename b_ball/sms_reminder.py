import os
from twilio.rest import Client
from b_ball.models import Player


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms_reminder():
    account_sid = 'TWILIO_ACCOUNT_SID'
    auth_token = 'TWILIO_AUTH_TOKEN'
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
                             body="Reminder- See you at B-Ball Tonight!!",
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)

