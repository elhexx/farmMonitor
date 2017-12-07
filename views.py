from main import app
from flask import render_template, request, jsonify
from ser import ArduinoSerial
from models import log
from time import sleep
con = None
import random
@app.before_first_request
def connect_serial():
    global con
    con = ArduinoSerial()

@app.route('/')
def index():
    return render_template('farm.html')

@app.route('/get/<name>')
def send(name):
    if name == 'all':
        vals = con.get_all_vals()

        vals_list = vals.split(',')
        vals_list[3] = vals_list[3].rstrip('\r\n')
        return jsonify(vals_list)


@app.route('/addLog')
def add():
    log('50', '50', '50')
    return "Done"

def getAll():
    con = ArduinoSerial()
    temp = con.get_temp().strip('\r\n')
    humd = con.get_Humd().strip('\r\n')
    sol_humd = con.get_solHumd().strip('\r\n')
    log(temp, humd, sol_humd)


if __name__ == '__main__':
    pass
