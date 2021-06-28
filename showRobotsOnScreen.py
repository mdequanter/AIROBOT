#python color_tracking.py --video balls.mp4
#python color_tracking.py

# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import urllib #for reading image from URL
import math
import urllib3
import time


greenX = 0
greenY = 0
blueX = 0
blueY=0
yellowX = 0
yellowY = 0
baseX=0
baseY=0


http = urllib3.PoolManager()

robotBlue = '192.168.1.103'
robotYellow = '192.168.1.101'
robotGreen = '192.168.1.102'

time.sleep(5)


def forward(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=70&right=110')

def backward(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=110&right=80')


def stop(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=90&right=90')

def left(ip):
    # open a connection to a URL using urllib2
    webUrl = http.request('GET','http://'+ip+'/?left=120&right=120')



def calculateDistance(x1,y1,x2,y2):
    #√[(x₂ - x₁)² + (y₂ - y₁)²],
    distance = math.sqrt(((x2-x1)*(x2-x1))+(y2-y1)*(y2-y1))
    return distance

# define the lower and upper boundaries of the colors in the HSV color space
lower = {'red':(166, 84, 141), 'green':(55, 90, 90), 'blue':(97, 100, 117), 'yellow':(23, 59, 119)} #assign new item lower['blue'] = (93, 10, 0)
upper = {'red':(186,255,255), 'green':(90,255,255), 'blue':(117,255,255), 'yellow':(54,255,255)}

# define standard colors for circle around the object
colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217)}

#pts = deque(maxlen=args["buffer"])

camera = cv2.VideoCapture(0)
# keep looping

frameCounter = 0

while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    frameCounter+=1

    if (frameCounter <= 5):
        continue
    else :
        frameCounter

    #IP webcam image stream
    #URL = 'http://10.254.254.102:8080/shot.jpg'
    #urllib.urlretrieve(URL, 'shot1.jpg')
    #frame = cv2.imread('shot1.jpg')


    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=1024)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    #for each color in dictionary check object in frame
    for key, value in upper.items():
        # construct a mask for the color from dictionary`1, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size. Correct this value for your obect's size
            if radius > 0.5:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius), colors[key], 2)
                cv2.putText(frame,"x:"+str(int(round(x,0)))+" y:"+str(int(round(y,0))), (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[key],2)
                if (key == 'blue') :
                    blueX= int(round(x,0))
                    blueY = int(round(y,0))
                if (key == 'yellow') :
                    yellowX= int(round(x,0))
                    yellowY = int(round(y,0))
                if (key == 'green') :
                    if (baseX == 0 and baseY==0) :
                        baseX=greenX
                        baseY=greenY
                    greenX= int(round(x,0))
                    greenY = int(round(y,0))


    distanceBlueGreen = calculateDistance(blueX,blueY,greenX,greenY)
    distanceGreenYellow = calculateDistance(greenX, greenY, yellowX, yellowY)

    if(greenY>1500 or greenY <200 or greenX>1500 or greenX<200) :
        left(robotGreen)
    else :
        forward(robotGreen)

    if (distanceBlueGreen < 80):
        backward(robotGreen)


    if (distanceGreenYellow < 80):
        backward(robotGreen)


    
    if (baseX > 0 and baseY>0) :
        if(greenY>(baseY+300) or greenY <(baseY-300) or greenX>(baseX+300) or greenX<(baseX-300)) :
            backward(robotGreen)
            time.sleep(1.5)
            left(robotGreen)
            time.sleep(0.75)
        else :
            forward(robotGreen)


    # show the frame to our screen
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()