from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import schedule
from threading import Thread
import time



app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.create_all()






from views import *


def run_every_10_seconds():
    getAll()
    print 'done'


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':

    schedule.every(5).seconds.do(run_every_10_seconds)
    t = Thread(target=run_schedule)
    t.start()
    app.run(host= '0.0.0.0', debug=True)