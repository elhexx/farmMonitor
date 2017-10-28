from flask import Flask, render_template

from ser import ArduinoSerial

app = Flask(__name__)



con = None

@app.before_first_request
def connect_serial():
    global con
    con = ArduinoSerial()



@app.route('/get/<name>')
def send(name):
    if name == 'temp' :
        return con.get_temp()
    if name == 'humd':
        return con.get_Humd()
    return name

@app.route('/')
def index():
    return render_template('farm.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)