from gpiozero import Servo, AngularServo
from time import sleep


class CustomServo:

    def __init__(self):
        pass

    def go_up(self, cm):
        print(f'going up {cm} cm...')

    def go_down(self, cm):
        print(f'going down {cm} cm...')