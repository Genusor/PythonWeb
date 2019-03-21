from bottle import route, run, view
from datetime import datetime as dt
from random import random


@route("/")
@view("predictions")
def index():
    now = dt.now()
    x = random()
    return {
        "date": f'{now.year}-{now.month}-{now.day}', 
    }

run(
    host="localhost",
    port=8000,
    autoreload=True
)