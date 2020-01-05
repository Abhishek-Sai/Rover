#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, json
import serial

# import camera driver
# if os.environ.get('CAMERA'):
from camera_opencv import Camera
global i
i = 0
# else:
#     from camera import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


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
    global i
    os.system('py ./hello.py ' + str(i))
    i = i + 1
    return "nothing"

@app.route('/to_arduino', methods=['POST'])
def to_arduino():
    print(request.form['key'])
    # ser = serial.Serial('COM6', 9600)
    # ser.write(request.form['key'].encode())
    return "nothing"


@app.route('/form_data', methods=['POST'])
def form_data():
    os.system('py ./latilongi.py ' + request.form['latitude'] + ' ' + request.form['longitude'])
    print(request.form['latitude'])
    print(request.form['longitude'])
    return "nothing"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', threaded=True)
