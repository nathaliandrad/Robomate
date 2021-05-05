import cv2 as cv
import time

cv.NamedWindow("camera",1)

capture = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(capture, 3, 360)
cv.SetCaptureProperty(capture, 4, 240)
while True:
    img = cv.QueryGrame(capture)
    cv.ShowImage("Camera", img)
    if cv.WaitKey(10) == 27:
        break