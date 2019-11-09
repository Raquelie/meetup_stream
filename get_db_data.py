"""
Test script for querying the DB
"""
from pony.orm import *
from create_db import Groups, DailyEvents
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=False)
from datetime import datetime, timedelta, date


@db_session
def get_events():
    # data = db.select("select * from DailyEvents")
    # print(data)
    # groups = db.select("select * from Groups")
    # print(groups)
    # delete(e for e in DailyEvents if e.date < datetime.now() - timedelta(days=2))
    # data = db.select("select * from DailyEvents")
    # print(data)
    result = select((s.city, count(s)) for s in DailyEvents if s.date.date() == date.today()).order_by(-2)
    for city in result[:10]:
        print(city[0], city[1])


get_events()