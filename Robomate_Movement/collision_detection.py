import time
from gpiozero import DistanceSensor
from gpiozero import PWMOutputDevice
from time import sleep

sensor1 = DistanceSensor(echo=24, trigger=23)

PWM_FORWARD_LEFT_PIN = 8
PWM_REVERSE_LEFT_PIN = 7

PWM_FORWARD_RIGHT_PIN = 10
PWM_REVERSE_RIGHT_PIN = 9

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def stop():
        forwardLeft.value = 0
        reverseLeft.value = 0
        forwardRight.value = 0
        reverseRight.value = 0
        
def forward():
        forwardLeft.value = .7
        reverseLeft.value = 0
        forwardRight.value = 0.6
        reverseRight.value = 0
        
def reverse():
        forwardLeft.value = 0
        reverseLeft.value = 0.7
        forwardRight.value = 0
        reverseRight.value = 0.6
        
def left():
        forwardLeft.value = 0.3
        reverseLeft.value = 0
        forwardRight.value = 0.7
        reverseRight.value = 0
        
def right():
        forwardLeft.value = 0.7
        reverseLeft.value = 0
        forwardRight.value = 0.3
        reverseRight.value = 0
        

while True:
    distance_to_object = sensor1.distance * 100
    
    
    if distance_to_object <= 40:
        reverse()
        time.sleep(0.5)
        right()
        time.sleep(0.5)
    else:
        forward()
        time.sleep(0.1)
        
        
        
        
        
        
        
        
        
        
        
        
        


