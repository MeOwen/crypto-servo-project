import atexit
from gpiozero import Device, Servo, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

"""
Values for servo movement can be calibrated here.
This depends on the physical setup.
ex. servo.move(cm=-10) should move the weight attached to
the servo down by 10 centimeters.
"""

class CustomServo:

    def __init__(self):
        
        self.ANGLE_UP = 106
        self.ANGLE_DOWN = 63
                
        self.GO_TIME_UP = 5
        self.GO_TIME_DOWN = 5

    def move(self, cm):
        
        print(f'moving {cm} cm...')
        self.servo = self.create_servo()

        if cm >= 0:
            self.servo.angle = self.ANGLE_UP
            sleep(self.GO_TIME_UP)
        else:
            self.servo.angle = self.ANGLE_DOWN
            sleep(self.GO_TIME_DOWN)

        del self.servo

    def create_servo(self):
        return AngularServo(
            'GPIO4',
            pin_factory=PiGPIOFactory(),
            min_angle=0,
            max_angle=180
        )

    @atexit.register
    def remove_servo():
        if self.servo:
            del self.servo