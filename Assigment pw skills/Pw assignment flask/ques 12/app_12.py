from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime

#background thread
thread = None
thread_lock = Lock()

app = Flask(__name__)
app.config['SECRET KEY'] = 'shanky'

socketio = SocketIO(app, cors_allowed_origins = '*')

#get current data andtime

def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%y %H:%M:%S")

#generate random sequence of dummy sensor values and send it to our clients

def background_thread():
    print("generating random sensor values")
    while True:
        dummy_sensor_value = round(random()*100,3)
        socketio.emit("updateSensorData", {"value": dummy_sensor_value, "date": get_current_datetime()})
        socketio.sleep(1)

#server root index file
@app.route("/")
def index():
    return render_template('index.html')

#decorator for connect
@socketio.on("connect")
def connect():
    global thread
    print("client connected")

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

#decorator for disconnect
@socketio.on("disconnect")
def disconnect():
    print("client disconnected", request.sid)

if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0",port=8000)