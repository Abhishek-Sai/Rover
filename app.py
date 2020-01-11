#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, json
import serial
import threading
import datetime
import time
import subprocess
import signal
import psutil

# from check import get_data

global now
global data
import tempfile


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def task1():
    while True:
        global now
        now = datetime.datetime.now()
        print("Current Time =", now)
        time.sleep(10)


def task2():
    app.run(host='0.0.0.0', port=5000)


def task3():
    global data
    temp = 0
    while True:
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(['py', 'D:\\Work\\rover_gui\\sma.py'], stdout=tempf, shell=True)
            proc.wait()
            tempf.seek(0)
            data = tempf.read().decode()
            # os.killpg(os.getpgid(proc.pid), signal.SIGINT) # For Linux


# import camera driver
# if os.environ.get('CAMERA'):
from camera_opencv import Camera

global i
i = 0
global j
j = 0

app = Flask(__name__)


@app.route('/pag1')
def index():
    """Video streaming home page."""
    return render_template('index1.html')


@app.route('/page2')
def index():
    """Video streaming home page."""
    return render_template('index2.html')


@app.route('/page3')
def index():
    """Video streaming home page."""
    return render_template('index3.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/background_process_test')
def background_process_test():
    print("Entered 1")
    os.system('py ./photo.py ')
    print("Finished")
    return "nothing"


@app.route('/get_data')
def get_data():
    global data
    return str(data)


@app.route('/to_arduino', methods=['POST'])
def to_arduino():
    print(request.form['key'])
    # ser = serial.Serial('COM6', 9600)
    # ser.write(request.form['key'].encode())
    # ser.close()
    return "nothing"


@app.route('/form_data', methods=['POST'])
def form_data():
    os.system('py ./latilongi.py ' + request.form['latitude'] + ' ' + request.form['longitude'])
    print(request.form['latitude'])
    print(request.form['longitude'])
    return "nothing"


if __name__ == '__main__':
    # app.run(debug=True)
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task3, name='t2')
    t3 = threading.Thread(target=task2, name='t3')

    # starting threads
    t1.start()
    t2.start()
    t3.start()

    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
