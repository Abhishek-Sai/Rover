import serial
import time

# set up the serial line

# Read and record the data
# empty list to store the data

while True:
    data = []
    ser = serial.Serial('COM11', 9600)
    b = ser.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    res = string.split()
    # flt = float(string)
    if res[0] == 'ang':
        angle = res[1]
        #print(angle)
    if res == 'INVALID':
        print("invalid")
    else:
        data.append(str(res))
        print(str(res))
        # time.sleep(2)  # wait (sleep) 0.1 seconds
    ser.close()
