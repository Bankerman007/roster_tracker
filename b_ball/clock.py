from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='fri', hour=23)
def scheduled_job():
    pass
    print('This job is run every Tuesday at 11pm.')

sched.start()
