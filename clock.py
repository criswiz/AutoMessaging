from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from love_honey import love_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(love_message, 'interval', seconds=10)

sched.start()
