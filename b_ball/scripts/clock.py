from django.utils import timezone
from datetime import date, datetime
from b_ball.scripts.reset_wkly_db import delete_players
from b_ball.scripts.save_to_db import start_db_save


def save_to_db():
    today = datetime.today()
    day = today.weekday()
    if day == 1:
        start_db_save()
    else:
        pass
    #('This job runs every Tuesday night at 11pm')
save_to_db()

def reset_players():
    today = datetime.today()
    day = today.weekday()    
    if day == 2:
        delete_players()
    else:
        pass
    #('This job runs every Wednesday night at 11pm')
reset_players()