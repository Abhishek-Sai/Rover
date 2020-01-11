import cv2
import serial
import time

ser = serial.Serial('COM6', 9600)

t = 0
while t <= 180:
    camera = cv2.VideoCapture(1)
    return_value, image = camera.read()
    cv2.imwrite('images/'+str(t) + 'cameraImage'+str('.png'), image)
    t = t + 30
    print(t)
    ser.write(str(t).encode())
    time.sleep(5)  # Check practically

ser.close()