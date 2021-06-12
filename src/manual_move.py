from servo import CustomServo

while True:
    i = input('enter cm to move: ')
    servo = CustomServo()
    servo.move(cm=float(i))