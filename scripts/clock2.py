from datetime import datetime
from b_ball.need_players_sms import players_needed
from b_ball.sms_all import sms_all
from b_ball.sms_reminder import sms_reminder
from b_ball.sms_pay_reminder import sms_pay_reminder
from b_ball.models import TurnOff


def run(*args):
    today = datetime.today()
    day = today.weekday()
    now = datetime.now()
    current_hour = int(now.strftime("%H%M"))
    flag = TurnOff.objects.all(pk=2)
    test = flag.on_off
    
    if test == True:

        if day == 6:
            sms_reminder()
    
        if day == 0 and current_hour >= 1055 and current_hour <= 1105:
            sms_all()  #This job is run every Monday at 11am.

        if day == 0 and current_hour >= 1755 and current_hour <= 1805:
            sms_pay_reminder()  #This job is run every Monday at 6pm.    
        
        if day == 1 and current_hour >= 1055 and current_hour <= 1105:
            players_needed() #This job is run every Tuesday at 11am.
        
        if day == 1 and current_hour >= 1400 and current_hour <= 1405:
            sms_reminder()  #This job is run every Tuesday at 2pm.