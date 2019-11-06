from pony.orm import *
db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=False)


@db_session
def get_events():
    data = db.select("select * from DailyEvents")
    print(data)
    groups = db.select("select * from Groups")
    print(groups)

get_events()