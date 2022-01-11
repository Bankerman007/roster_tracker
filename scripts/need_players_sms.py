from b_ball. models import Player
from b_ball.models import Player_full_text_list
import os
from twilio.rest import Client



def players_needed():
    this_weeks_players_dict = Player.objects.values('player_name', 'player_cell')
    this_weeks_list = []

    for ele in this_weeks_players_dict:
        for key, value in ele.items():
            v = value
            this_weeks_list.append(v)

    twl = {this_weeks_list[i]: this_weeks_list[i + 1] for i in range(0, len(this_weeks_list), 2)}
    twl_value = list(twl.values())
        

    all_players_cells_dict = Player_full_text_list.objects.values('player_name_full_text','player_cell_full_text')
    all_players_list = []

    for ele in all_players_cells_dict:
        for key, value in ele.items():
            v = value
            all_players_list.append(v)

    apl = {all_players_list[i]: all_players_list[i + 1] for i in range(0, len(all_players_list), 2)}
    apl_value = list(apl.values())
        

    not_signed_up = set(apl_value).difference(twl_value)
    for m in not_signed_up:
        not_signed_up_list = Player.objects.get(player_cell = m)    
        
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
        
    for n in not_signed_up_list:
        send_cell = n
        print(send_cell)

        # message = client.messages \
        #                 .create(
        #                      body="Ballers Needed! Register for ball this weeek: b-ball-app.herokuapp.com/register_player/",
        #                      from_='+16467989631',
        #                      to= '+1'+ send_cell,
        #             )
    
        # print(message.sid)  
        
players_needed()