import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (600, 400)
    camera.start_preview()
    time.sleep(2)
    camera.capture('foo.jpg')