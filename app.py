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
from camera_opencv import Camera
import tempfile
import json

# from check import get_data

global now
global data
global i
i = 0
global j
j = 0
global ser
global ser1
global json_data
global c
c = 0


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
            proc = subprocess.Popen(['py', 'D:\\Work\\rover_gui\\check.py'], stdout=tempf, shell=True)
            proc.wait()
            tempf.seek(0)
            data = tempf.read().decode()
            # os.killpg(os.getpgid(proc.pid), signal.SIGINT) # For Linux


def task4():
    #global ser
    #ser = serial.Serial('COM5', 9600)
    return "hi"


def task5():
    global ser
    ser = serial.Serial('COM7', 9600)
    ser.flushInput()
    time.sleep(1)


app = Flask(__name__)


@app.route('/page1')
def index1():
    """Video streaming home page."""
    return render_template('index1.html')


@app.route('/page2')
def index2():
    """Video streaming home page."""
    return render_template('index2.html')


@app.route('/page3')
def index3():
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


# @app.route('/get_data')
# def get_data():
#     global ser1
#     global data
#     print(data)
#     if data is None:
#         return "nothing"
#     else:
#         return data



@app.route('/to_arduino', methods=['POST'])
def to_arduino():
    print(request.form['key'])
    global ser
    # if request.form['key'] == "119":
    #     ser.write(b'w')
    # elif request.form['key'] == "97":
    #     ser.write(b'a')
    #ser.write((request.form['key'] + "\n").encode())
    # ser.close()
    return "nothing"


@app.route('/form_data', methods=['POST'])
def form_data():
    os.system('py ./path.py ' + request.form['latitude'] + ' ' + request.form['longitude'])
    # print(request.form['latitude'])
    # print(request.form['longitude'])
    return "nothing"


if __name__ == '__main__':
    # app.run(debug=True)
    t1 = threading.Thread(target=task1, name='t1')
    #t2 = threading.Thread(target=task3, name='t2')
    t4 = threading.Thread(target=task4, name='t4')
    #t5 = threading.Thread(target=task5, name='t5')
    t3 = threading.Thread(target=task2, name='t3')

    # starting threads
    t1.start()
    #t2.start()
    t4.start()
    #t5.start()
    t3.start()

    # wait until all threads finish
    t1.join()
    #t2.join()
    t4.join()
    #t5.join()
    t3.join()
