# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)



while True:
	hue_value = int(raw_input("Hue Value: "))
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		lower_red = np.array([hue_value-10,100,100])
		upper_red = np.array([hue_value+10, 255, 255])

		mask = cv2.inRange(hsv, lower_red, upper_red)

		res = cv2.bitwise_and(image, image, mask= mask)

		cv2.imshow("Frame", image)
		cv2.imshow("Mask", mask)
		cv2.imshow("Res", res)

		rawCapture.truncate(0)

		k = cv2.waitKey(5) #& 0xFF
		if "q" == chr(k & 255):
			break
