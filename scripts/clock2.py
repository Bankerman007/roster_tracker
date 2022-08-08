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
    flag = TurnOff.objects.get(pk=1)
    should_run = flag.on_off
    
    if should_run:
        print('should run is true, excuting script')
    
        if day == 0 and current_hour >= 1055 and current_hour <= 1105:
            sms_all()  #This job is run every Monday at 11am.

        if day == 0 and current_hour >= 1755 and current_hour <= 1805:
            sms_pay_reminder()  #This job is run every Monday at 6pm.    
        
        if day == 0 and current_hour >= 1655 and current_hour <= 1705:
            players_needed() #This job is run every Monday at 5pm.
        
        if day == 1 and current_hour >= 1400 and current_hour <= 1405:
            sms_reminder()  #This job is run every Tuesday at 2pm.

    else:
        print('is not true, not executing script')