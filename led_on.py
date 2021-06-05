import time
from gpiozero import LED

led = LED('GPIO4')

while True:
	led.on()
	time.sleep(0.2)
	led.off()
	time.sleep(0.2)
