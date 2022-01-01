from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='tue', hour=23)
def scheduled_job():
    print('This job is run every Tuesday at 11pm.')

sched.start()
