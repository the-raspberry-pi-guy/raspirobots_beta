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

while True:
	while True:
		try:
			hue_value = int(raw_input("Hue Value: "))
		except ValueError:
			print("That isn't an integer, try again")
		else:
			break
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		lower_red = np.array([hue_value-10,100,100])
		upper_red = np.array([hue_value+10, 255, 255])

		color_mask = cv2.inRange(hsv, lower_red, upper_red)

		result = cv2.bitwise_and(image, image, mask= color_mask)

		cv2.imshow("Camera Output", image)
		cv2.imshow("Color Mask", color_mask)
		cv2.imshow("Final Result", result)

		rawCapture.truncate(0)

		k = cv2.waitKey(5) #& 0xFF
		if "q" == chr(k & 255):
			break
