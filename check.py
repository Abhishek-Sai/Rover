import serial
import time
import json
global json_data
data = {}
ser = serial.Serial('COM6', 9600)
b = ser.readline()  # read a byte string
string_n = b.decode()  # decode byte string into Unicode
string = string_n.rstrip()  # remove \n and \r
res = string.split()
if res[0] != "INVALID":
    if res[0] == "lat":
        latitude = res[1]
        #data.append(latitude)
        # print(latitude)
        data['latitude'] = latitude
        json_data = json.dumps(data)
        # data.append(latitude)
    if res[2] == "lon":
        longitude = res[3]
        # print(longitude)
        #data.append(longitude)
        data['longitude'] = longitude
        json_data = json.dumps(data)
        # data.append(longitude)
    if res[4] == "ang":
        angle = res[5]
        #data.append(angle)
        # print(angle)
        data['angle'] = angle
        json_data = json.dumps(data)
        # data.append(angle)
print(string)
ser.close()

