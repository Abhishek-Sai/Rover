from router import router
import serial as serial

from sensor import sensorData
from math import *
from time import sleep
import sys

F = 119
R = 100
L = 97
S = 115
# import the python files having gps, encoder, final coordinates and imu functions

ser1 = serial.Serial('/dev/ttyACM1', 115200, timeout=0.1)

global x
global angle


def dist(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742000 * asin(sqrt(a))  # 2 * R * asin...


# x = front()
global FX
global FY
FX = float(sys.argv[1])
FY = float(sys.argv[2])

x = sensorData()
print("X is "+str(x))
global SX
global SY

SX = x[0]
SY = x[1]
print("SX is "+str(x[0]))
print("SY is "+str(x[1]))
#d = dist(SX, SY, FX, FY)


def left(angle):
    global x

    x = sensorData()
    a = x[2]
    y = router()
    routerang = y
    while a + 5 < angle < a - 5:
        ser1.write((str(L) + "\n").encode())
        ser1.write(routerang)


def right(ang):
    global x
    x = sensorData()
    a = x[2]
    y = router()
    routerang = y
    while a - 5 < ang < a + 5:
        ser1.write((str(R) + "\n").encode())
        angle = x[2]
        ser1.write(routerang)


while d > 5:
    dlat = FX - float(SX)
    dlon = FY - float(SY)
    angle1 = degrees(atan2((sin(dlon) * cos(FX)), ((cos(float(SX)) * sin(FX)) - (sin(float(SX)) * cos(FX) * cos(dlon)))))
    if angle1 < 0:
        angle1 = angle1 + 360
    x = sensorData()
    angle2 = x[2]

    if angle1 > angle2 and angle2 <= angle1 + 180:
        angle = angle2 - angle1  # left
        left(angle)


    elif angle2 > angle1 + 180:
        angle = 360 - angle2 + angle1  # right
        right(angle)

    elif angle2 < angle1:
        angle = angle1 - angle2  # right
        right(angle)

    ser1.write((str(F) + "\n").encode())
    sleep(3)

    x = sensorData()
    global SX
    global SY
    SX = x[0]
    SY = x[1]
    d = dist(float(SX), float(SY), FX, FY)