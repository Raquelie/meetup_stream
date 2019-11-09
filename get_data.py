from flask import Flask, request
from create_db import Groups, DailyEvents
from datetime import date, datetime

from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='database.sqlite')


app = Flask(__name__)


@app.route('/near')
def near_meetups():
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    num = request.args.get('num')
    return get_near_groups(lon, lat, num)


@app.route('/topCities/<num>')
def top_cities(num):
    print(num)
    return get_top_cities(num)


@db_session
def get_top_cities(n):
    result = select((s.city, count(s)) for s in DailyEvents if s.date.date() == date.today()).order_by(-2)
    output = ''
    start = True
    for city in result[:int(n)]:
        if start:
            output = output + city[0]
            start = False
        else:
            output = output + ' - ' + city[0]
    return output


@db_session
def get_near_groups(lon, lat, n):
    return 'TODO'


if __name__ == '__main__':
    app.run(debug=True)
