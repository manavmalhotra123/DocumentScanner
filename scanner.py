import cv2 
import numpy as np 
import utils 

# setting up the camera
camera = cv2.VideoCapture(0)
# fixing the resolution
camera.set(10,160)

heightImage = 540
WidthImage  = 480

utils.initializeTrackbars()
count = 1