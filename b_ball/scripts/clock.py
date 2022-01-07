from django.utils import timezone
from datetime import date, datetime


def full_list_text():
    pass #sms_all()
    #('This job is run every Sunday at 9pm.')

def reminder_text():
    pass #sms_reminder()
    #('This job is run every Tuesday at 11am.')

def save_to_db():
    today = datetime.today()
    day = today.weekday()
    #time = datetime.time()
    #run_time = datetime.time(hour= 3, minute = 0, second = 0)
    if day == 4:
        save_to_db()
    else:
        pass

save_to_db()

def reset():
    pass #delete_players()
    #('This job is run every Tuesday at 11pm to reset weekly player list.')

# def run(*args):
#   date = '2021-10-26'
#   EmailSender.send_email(datetime.today())

