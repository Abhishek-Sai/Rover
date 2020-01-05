import serial
import time


# set up the serial line

# Read and record the data
# empty list to store the data
def angle():
    ser = serial.Serial('COM11', 115200)
    time.sleep(2)
    data = []
    b = ser.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    res = string.split()
    # flt = float(string)
    if (res[0] == 'ang'):
        angle = res[1]
        # print(angle)
    data.append(str(res))
    f = open("log1.txt", "a+")
    f.write(string)

    # print(string)
    time.sleep(0.1)  # wait (sleep) 0.1 seconds
    ser.close()
    return angle


# def coordinates():
#     ser = serial.Serial('COM5', 115200)
#     time.sleep(2)
#     data = []
#     gps = []
#     b = ser.readline()  # read a byte string
#     string_n = b.decode()  # decode byte string into Unicode
#     string = string_n.rstrip()  # remove \n and \r
#     res = string.split()
#     # flt = float(string)
#     if (res[0] == 'lat'):
#         latitude = res[1]
#     if (res[0] == 'lon'):
#         longitude = res[1]
#     gps.append(latitude)
#     gps.append(longitude)
#     data.append(str(res))
#     print(string)
#     time.sleep(0.1)  # wait (sleep) 0.1 seconds
#     ser.close()
#     return gps

y = angle()
print(y)
