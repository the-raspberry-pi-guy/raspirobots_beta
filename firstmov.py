import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

for i in range(4):
	robot.forward(0.5)
	time.sleep(0.5)
	robot.right(0.5)
	time.sleep(0.25)
