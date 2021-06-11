from time import sleep
from servo import CustomServo

"""
This can be used to fine tune up & down speeds in servo.py
"""

while True:
    servo = CustomServo()
    servo.move(cm=1)
    sleep(0.5)
    servo.move(cm=-1)
    sleep(0.5)
