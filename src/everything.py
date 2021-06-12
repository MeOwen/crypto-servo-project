import time
import cryptocompare
from servo import CustomServo

time_interval = 60
current_price = 0
last_price = 0

cm_range = 100
usd_range = 1000
# usd_range = 100000
usd_cm_ratio = cm_range / usd_range

initial_run = True

def get_price():
    return cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']

def get_cm_from_usd_difference(price_difference):
    return price_difference * usd_cm_ratio

while True:

    last_price = current_price
    current_price = get_price()
    price_difference = current_price - last_price

    cm_difference = get_cm_from_usd_difference(
        price_difference=price_difference
    )

    if not initial_run:

        print('\n')
        print(f'last_price: {"%.2f" % last_price}')
        print(f'current_price: {"%.2f" % current_price}')
        print(f'usd difference: {"%.2f" % price_difference}')
        print(f'cm difference: {"%.2f" % cm_difference}')

        servo = CustomServo()
        servo.move(cm=cm_difference)

    if initial_run:
        initial_run = False

        
    time.sleep(time_interval)
