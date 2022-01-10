import os
from twilio.rest import Client
from b_ball.save_to_db import all_cells



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms_all():
    account_sid = 'AC7d0ce7af110c2d84da65e506722c1f2d'
    auth_token = '21d2b9c70be435ee1a1869a1f452e145'
    client = Client(account_sid, auth_token)
    [apl_value] = all_cells()
    all_players = apl_value
    for p in all_players:
        send_cell = p

        message = client.messages \
                        .create(
                             body="Ballers Needed! Register for ball this weeek: b-ball-app.herokuapp.com/register_player/",
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)

