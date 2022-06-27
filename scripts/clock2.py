from datetime import datetime
from b_ball.need_players_sms import players_needed
from b_ball.sms_all import sms_all
from b_ball.sms_reminder import sms_reminder


def run(*args):
    today = datetime.today()
    day = today.weekday()
    now = datetime.now()
    current_hour = int(now.strftime("%H%M"))
    
    if day == 0 and current_hour >= 1055 and current_hour <= 1120:
        sms_all()  #This job is run every Monday at 11am.
    
    if day == 1 and current_hour >= 1155 and current_hour <= 1205:
        players_needed() #This job is run every Tuesday at 11am.
    
    if day == 1 and current_hour >= 1355 and current_hour <= 1410:
        sms_reminder()  #This job is run every Tuesday at 2pm.
    

