# Python code for Multiple Color Detection

import numpy as np
import cv2
from PIL import Image
import time
import psutil


# Capturing video through webcam
webcam = cv2.VideoCapture(0)
countRed = 0
countYellow = 0
countGreen = 0
isRed = False
img_red = Image.open("/home/pi/Desktop/BIG_EYES/robored.png")
img_yellow = Image.open("/home/pi/Desktop/BIG_EYES/roboblue.png")
img_green = Image.open("/home/pi/Desktop/BIG_EYES/robogreen.png")
video = cv2.VideoCapture("/home/pi/Desktop/color/whites.mov")

# Start a while loop
while(1):

    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for red color and
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for dark GREEn  color and
    # define mask
    yellow_lower = np.array([77, 83, 11], np.uint8)
    yellow_upper = np.array([109, 229, 73], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # Set range for blue color and
    # define mask
    #    blue_lower = np.array([94, 80, 2], np.uint8)
    #blue_upper = np.array([120, 255, 255], np.uint8)
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)
    

    # For yellow color
    yellow_mask = cv2.dilate(yellow_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask=yellow_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask=blue_mask)




    # Creating contour to track red color
    hierarchy, contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        if(countYellow == 1 and countGreen == 1):
            countYellow = 0
            countGreen = 0
        if(countRed < 1):
            print("Red Color")
            img_red.show()
            countRed += 1
            countYellow = 0
            countGreen = 0
            
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
            
                    
           # countRed = 0
            #countYellow = 0
            # if(countGreen > 0):
            #     countGreen = 0

        # cv2.putText(imageFrame, "Red Colour", (x, y),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1.0,
        #             (0, 0, 255))



    # Creating contour to track green color
    hierarchy, contours, hierarchy = cv2.findContours(yellow_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    
    for pic, contour in enumerate(contours):
        
        if(countYellow == 1 and countRed == 1):
            countYellow = 0
            countRed = 0
        if(countGreen < 1):
            print("Green color")
            img_green.show()
            countGreen += 1
            countYellow = 0
            countRed = 0
            
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        
        

    # Creating contour to track blue color
    hierarchy, contours, hierarchy = cv2.findContours(blue_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
     
    for pic, contour in enumerate(contours):
        if(countRed == 1 and countGreen == 1):
            countRed = 0
            countGreen = 0
        if(countYellow<1):
            print("Blue Color")
            img_yellow.show()
            countYellow += 1
            countRed = 0
            countGreen = 0
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()
        
             
             
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
