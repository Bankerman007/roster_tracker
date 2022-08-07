from datetime import datetime
from b_ball.reset_wkly_db import delete_players
from b_ball.save_to_db import start_db_save
from b_ball.models import TurnOff


def run(*args):
    test = TurnOff.objects.all()
    today = datetime.today()
    day = today.weekday()
    
    if test == False:
        if day == 1:
            start_db_save()  #('This job runs every Tuesday night at 11pm')
        if day == 2:
            delete_players()  #('This job runs every Wednesday night at 11pm')
           
