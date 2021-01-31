import numpy as np
import cv2


def nothing(x):
    pass


def make_mask(hsv_frame, color_range):
    mask = cv2.inRange(hsv_frame, color_range[0], color_range[1])
    eroded = cv2.erode(mask, kernel, iterations=1)
    dilated = cv2.dilate(eroded, kernel, iterations=1)
    return dilated


kernel = np.zeros((300, 512, 3), np.uint8)
name = 'Calibrate'
cv2.namedWindow(name)
cv2.createTrackbar('Hue', name, 0, 255, nothing)
cv2.createTrackbar('Sat', name, 0, 255, nothing)
cv2.createTrackbar('Val', name, 0, 255, nothing)

switch = '0 : OFF \n 1: ON'

cv2.createTrackbar(switch, name, 0, 1, nothing)

while (1):
    cv2.imshow(name, kernel)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    hue = cv2.getTrackbarPos('Hue', name)
    sat = cv2.getTrackbarPos('Sat', name)
    val = cv2.getTrackbarPos('Val', name)
    s = cv2.getTrackbarPos(switch, name)

    if s == 0:
        kernel[:] = 0
    else:
        kernel[:] = [hue, sat, val]
# cap = cv2.VideoCapture(0)
#
# while (True):
#     _, frameinv = cap.read()
#     frame = cv2.flip(frameinv, 1)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     cv2.imshow('frame', hsv)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#
# cap.release()
cv2.destroyAllWindows()
