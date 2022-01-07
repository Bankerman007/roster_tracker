from datetime import date, datetime
from b_ball.scripts.sms_all import sms_all
from b_ball.scripts.sms_reminder import sms_reminder

def full_list_text():
    today = datetime.today()
    day = today.weekday()
    if day == 0:
        sms_all()
    else:
        pass
    #('This job is run every Monday at 10am.')
full_list_text()

def reminder_text():
    today = datetime.today()
    day = today.weekday()
    if day == 1:
        sms_reminder()
    else:
        pass
    #('This job is run every Tuesday at 10am.')

reminder_text()