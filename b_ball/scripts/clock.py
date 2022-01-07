from django.utils import timezone
from datetime import date, datetime
from b_ball.scripts.reset_wkly_db import delete_players
from b_ball.scripts.save_to_db import start_db_save


def full_list_text():
    pass #sms_all()
    #('This job is run every Sunday at 9pm.')

def reminder_text():
    pass #sms_reminder()
    #('This job is run every Tuesday at 11am.')

def save_to_db():
    today = datetime.today()
    day = today.weekday()
    if day == 3:
        start_db_save()
    else:
        pass

def reset_players():
    today = datetime.today()
    day = today.weekday()    
    if day==4:
         print("Scott, this worked!!")
        #delete_players()
    else:
        pass

reset_players()
     
    
  
    # if day == 4:
    #     delete_players()
    # else:
    #     pass
    #('This job is run every Tuesday at 11pm to reset weekly player list.')



# def run(*args):
#   date = '2021-10-26'
#   EmailSender.send_email(datetime.today())

save_to_db()