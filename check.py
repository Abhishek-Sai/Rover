import serial
import time
import json
data = {}
ser = serial.Serial('COM7', 9600)
b = ser.readline()  # read a byte string
string_n = b.decode()  # decode byte string into Unicode
string = string_n.rstrip()  # remove \n and \r
res = string.split()
if res[0] == "INVALID":
    if res[1] == "lat":
        latitude = res[2]
        # print(latitude)
        data['latitude'] = latitude
        json_data = json.dumps(data)
        # data.append(latitude)
    if res[3] == "lon":
        longitude = res[4]
        # print(longitude)
        data['longitude'] = longitude
        json_data = json.dumps(data)
        # data.append(longitude)
    if res[5] == "ang":
        angle = res[6]
        # print(angle)
        data['angle'] = angle
        json_data = json.dumps(data)
        # data.append(angle)
print(json_data)

