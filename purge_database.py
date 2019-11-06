from pony.orm import *
from datetime import datetime

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=False)


