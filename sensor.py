import serial
import time


def sensorData():
    ser = serial.Serial('COM6', 9600)
    data = []
    time.sleep(1)
    b = ser.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    res = string.split()
    if res[0] != "INVALID":
        if res[0] == "lat":
            latitude = res[1]
            print(latitude)
            data.append(latitude)
        if res[2] == "lon":
            longitude = res[3]
            print(longitude)
            data.append(longitude)
        if res[4] == "ang":
            angle = res[5]
            print(angle)
            data.append(angle)
        return data
    ser.close()

