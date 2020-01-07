import cv2
import sys
camera = cv2.VideoCapture(0)
return_value, image = camera.read()
#number = int(sys.argv[1])
cv2.imwrite('cameraImage.png', image)