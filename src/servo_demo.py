from gpiozero import Servo, AngularServo
from time import sleep


def log():
    print("angle: {}\tpulse width: {}".format(servo.angle, servo.pulse_width))


servo = AngularServo('GPIO4', min_angle=0, max_angle=180)
SLOW_RIGHT = 60
STOP = 72
SLOW_LEFT = 85

FAST_RIGHT = 40
FAST_LEFT = 105

GO_TIME = 20
STOP_TIME = 1

while True:

    servo.angle = FAST_RIGHT
    log()
    sleep(GO_TIME)

    servo.angle = STOP
    log()
    sleep(STOP_TIME)

    servo.angle = FAST_LEFT
    log()
    sleep(GO_TIME)

    servo.angle = STOP
    log()
    sleep(STOP_TIME)



def input_angle():
    a = input("enter angle: ")
    servo.angle = a
    log()
    sleep(3)

