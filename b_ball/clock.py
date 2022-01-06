from apscheduler.schedulers.blocking import BlockingScheduler
from b_ball.reset_wkly_db import delete_players

from b_ball.sms_all import sms_all
from b_ball.sms_reminder import sms_reminder

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun', hour=21)
def full_list_text():
    pass #sms_all()
    #('This job is run every Sunday at 9pm.')

@sched.scheduled_job('cron', day_of_week= 'tue', hour=11)
def reminder_text():
    pass #sms_reminder()
    #('This job is run every Tuesday at 11am.')

@sched.scheduled_job('cron', day_of_week= 'thu', hour=20.30)
def save_to_db():
    save_to_db()

@sched.scheduled_job('cron', day_of_week= 'tue', hour=23)
def reset():
    pass #delete_players()
    #('This job is run every Tuesday at 11pm to reset weekly player list.')

sched.start()
