import os
import cv2
from base_camera import BaseCamera
import datetime
import numpy as np
global i
i = 0

# class Camera1(BaseCamera):
#     video_source = 0
#
#     @staticmethod
#     def set_video_source(source):
#         Camera1.video_source = source[0]
#
#     @staticmethod
#     def frames():
#         camera = cv2.VideoCapture(Camera1.video_source)
#         if not camera.isOpened():
#             raise RuntimeError('Could not start camera.')
#
#         while True:
#             # read current frame
#             _, img1 = camera.read()
#
#             # encode as a jpeg image and return it
#             yield cv2.imencode('.jpg', img1)[1].tobytes()
#
#
# class Camera2(BaseCamera):
#     video_source = 1
#
#     @staticmethod
#     def set_video_source(source):
#         Camera2.video_source = source[1]
#
#     @staticmethod
#     def frames():
#         camera = cv2.VideoCapture(Camera2.video_source)
#         if not camera.isOpened():
#             raise RuntimeError('Could not start camera.')
#
#         while True:
#             # read current frame
#             _, img2 = camera.read()
#
#             # encode as a jpeg image and return it
#             yield cv2.imencode('.jpg', img2)[1].tobytes()

class Camera(BaseCamera):
    video_source1 = 0

    # video_source2 = 1

    @staticmethod
    def set_video_source(source):
        Camera.video_source1 = source[0]
        # Camera.video_source2 = source[1]
    @staticmethod
    def frames():
        camera1 = cv2.VideoCapture(Camera.video_source1)
        # camera2 = cv2.VideoCapture(Camera.video_source2)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        if not (camera1.isOpened()):
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img1 = camera1.read()
            # _, img2 = camera2.read()
            img1 = cv2.resize(img1, (704, 396))
            # img2 = cv2.resize(img2, (704, 396))
            # img = np.hstack((img1, img2))

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img1)[1].tobytes()

            ret, frame = camera1.read()
            # output the frame
            out.write(frame)
