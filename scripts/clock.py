from datetime import datetime
from b_ball.reset_wkly_db import delete_players
from b_ball.save_to_db import start_db_save
from multiprocessing import Process



def run(*args):
    today = datetime.today()
    day = today.weekday()
    if day == 1:
        start_db_save()  #('This job runs every Tuesday night at 11pm')
    if day == 2:
        delete_players()  #('This job runs every Wednesday night at 11pm')
           
