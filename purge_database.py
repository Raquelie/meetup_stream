import schedule
import time
from pony.orm import *
from create_db import Groups, DailyEvents
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=False)
from datetime import datetime, timedelta


@db_session
def delete_events():
    delete(e for e in DailyEvents if e.date < datetime.now() - timedelta(days=2))
    print("Events deleted from previous days...")


def job():
    delete_events()


schedule.every().day.at("00:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

