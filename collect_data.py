#!/usr/bin/env python3
import os
import websocket
import json
import time
from datetime import datetime
from create_db import Groups, DailyEvents
from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='database.sqlite')


# Check if the group exists and add it if it doesn't
def check_new_group(group_id):
    @db_session
    def get_groups():
        groups = select(g for g in Groups if g.group_id == group_id)
        return len(groups)
    n = get_groups()
    if n > 0:
        return True
    else:
        return False


def save_to_database(dict_data):
    @db_session
    def insert_data():
        # Check if group needs to be inserted
        flag_group = check_new_group(dict_data['group']['group_id'])
        if not flag_group:
            db.insert("Groups", group_id = dict_data['group']['group_id'],
                      name=dict_data['group']['group_name'],
                      city=dict_data['group']['group_city'],
                      country=dict_data['group']['group_country'],
                      lon=dict_data['group']['group_lon'],
                      lat=dict_data['group']['group_lat'])
        # Insert the event
        db.insert("DailyEvents",  date=datetime.now(), city=dict_data['group']['group_city'],
                  country=dict_data['group']['group_country'], group_id=dict_data['group']['group_id'])

    insert_data()


def on_message(ws, message):
    dict_m = json.loads(message)
    save_to_database(dict_m)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("CLOSED")


websocket.enableTrace(True)


while 1:
    ws = websocket.WebSocketApp("ws://stream.meetup.com/2/rsvps",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
    print("Connection closed, retrying in 10 sec ...")
    time.sleep(10)