import cv2
import numpy as np

# differentiating colors on the basis of HSV

# the lower and upper range for RED color
red_lower = np.array([0, 70, 50])
red_upper = np.array([10, 255, 255])

# the lower and upper range for BLUE color
blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])

# the lower and upper range for GREEN color
green_lower = np.array([35, 25, 25])
green_upper = np.array([86, 255, 255])

# the lower and upper range for YELLOW color
yellow_lower = np.array([15, 150, 20])
yellow_upper = np.array([35, 255, 255])

# detecting colors through the webcam
# this will capture webcam footage and store in video variable
video = cv2.VideoCapture(0)

# as we need to run the following code endlessly for capturing our webcam
# footage, otherwise it will only allow the one frame of webcam
while True:
    # it reads our video object
    # then new image will get stored in 'img' variable
    success, img = video.read()
    # since opencv stores image in bgr format
    # we are converting our image to hsv and store in a new 'image'variable
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #  'mask' object will find and separate the color we want from the
    #  original img
    red_mask = cv2.inRange(image, red_lower, red_upper)
    blue_mask = cv2.inRange(image, blue_lower, blue_upper)
    green_mask = cv2.inRange(image, green_lower, green_upper)
    yellow_mask = cv2.inRange(image, yellow_lower, yellow_upper)

    # /*********************************************************\
    # TO GET THE COORDINATES OF THE OBJECT
    # contours, hierarchy = cv2.findContours(
    #     mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    # )

    # if len(contours) != 0:
    #     for contour in contours:
    #         if cv2.contourArea(contour) > 500:
    #             x, y, w, h = cv2.boundingRect(contour)
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # /*********************************************************\

    cv2.imshow("red_mask", red_mask)
    cv2.imshow("blue_mask", blue_mask)
    cv2.imshow("green_mask", green_mask)
    cv2.imshow("yellow_mask", yellow_mask)

    cv2.imshow("webcam", img)

    cv2.waitKey(1)

