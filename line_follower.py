import gpiozero
import time

SPEED = 0.25

robot = gpiozero.Robot(left=(17,18), right=(27,22))

left = gpiozero.DigitalInputDevice(9)
right = gpiozero.DigitalInputDevice(11)

while True:
	# Both sensors read white
	if (left.is_active == True) and (right.is_active == True):
		robot.forward(SPEED)
	# Left sensor detects the line
	elif (left.is_active == False) and (right.is_active == True):
		robot.right(SPEED)
	# Right sensor detects the line
	elif (left.is_active == True) and (right.is_active == False):
		robot.left(SPEED)
	# Only option left: both sensors detect line
	else:
		robot.stop()
