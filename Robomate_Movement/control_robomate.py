from gpiozero import Robot
from bluedot import BlueDot

robomate = Robot((8,7),(10,9))
bd = BlueDot()


def move(pos):
    if pos.top:
        robomate.forward()
    elif pos.bottom:
        robomate.backward()
    elif pos.right:
        robomate.right()
    elif pos.left:
        robomate.left()
        

def stop():
    robomate.stop()
    
    
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop