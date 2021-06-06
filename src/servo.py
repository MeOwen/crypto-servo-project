from gpiozero import Device, Servo, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


class CustomServo:

    def __init__(self):
        
        self.servo = AngularServo(
            'GPIO4',
            pin_factory=PiGPIOFactory(),
            min_angle=0,
            max_angle=180
        )
        
        self.SLOW_RIGHT = 60
        self.SLOW_LEFT = 85
        
        self.FAST_RIGHT = 40
        self.FAST_LEFT = 105
        
        self.STOP = 72

        self.GO_TIME = 2
        self.STOP_TIME = 1

    def go_up(self, cm):
        print(f'going up {cm} cm...')
        self.servo.angle = self.SLOW_RIGHT
        sleep(self.GO_TIME)
        del self.servo

    def go_down(self, cm):
        print(f'going down {cm} cm...')