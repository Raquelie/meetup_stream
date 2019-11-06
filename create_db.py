from pony.orm import *
from datetime import datetime

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Groups(db.Entity):
    # change to PK when no duplicates
    group_id = Required(int)
    name = Required(str)
    city = Required(str)
    country = Required(str)
    lon = Required(float)
    lat = Required(float)


class DailyEvents(db.Entity):
    date = Required(datetime)
    city = Required(str)
    country = Required(str)
    group_id = Required(int)


sql_debug(True)
db.generate_mapping(create_tables=True)

