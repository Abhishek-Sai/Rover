import numpy as np
import pyautogui
import imutils
import cv2
import sys

number = int(sys.argv[1])
print(number)
pyautogui.screenshot(str(number)+"screenshot.png")
image = cv2.imread(str(number)+"screenshot.png")
cv2.imshow(str(number)+"Screenshot", imutils.resize(image, width=600))
cv2.waitKey(0)
