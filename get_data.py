import requests
from datetime import datetime
import os
from flask import Flask, flash, request, redirect
from flask import send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/near')
def near_meetups():
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    return str(int(lon)+int(lat))


@app.route('/topCities/<num>')
def top_cities(num):
    return num


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')