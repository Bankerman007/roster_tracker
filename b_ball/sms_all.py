import os
from twilio.rest import Client
from b_ball.models import Player_full_text_list



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms_all():
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
                             body= "This week is at Randall Oaks Rec Center, 500 N Randall Rd in West Dundee from 6-8pm.  Register for Tuesday ball, first 15 players get in. http://b-ball-app.herokuapp.com/",
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)

