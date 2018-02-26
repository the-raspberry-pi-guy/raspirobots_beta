import gpiozero
import time

led = gpiozero.LED(4)

while True:
        led.on()
        time.sleep(5)
        led.off()
        time.sleep(1)

