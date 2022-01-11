from datetime import date, datetime
from b_ball.sms_all import sms_all
from b_ball.sms_reminder import sms_reminder


def run(*args):
    today = datetime.today()
    day = today.weekday()
    if day == 1:
        sms_all()  #('This job is run every Monday at 10am.')
    if day == 3:
        sms_reminder()  #('This job is run every Tuesday at 10am.')

    

