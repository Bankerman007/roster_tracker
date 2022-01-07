import os
from twilio.rest import Client
from b_ball.scripts.save_to_db import save_to_db


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms_reminder():
    account_sid = 'AC7d0ce7af110c2d84da65e506722c1f2d'
    auth_token = '21d2b9c70be435ee1a1869a1f452e145'
    client = Client(account_sid, auth_token)
    [twl_value] = save_to_db()
    tw_players = twl_value
    for p in tw_players:
        send_cell = p

        message = client.messages \
                        .create(
                             body="test: reminder",
                             from_='+16467989631',
                             to= '+1'+ send_cell,
                    )
    
        print(message.sid)

sms_reminder()