import time
import cryptocompare

while True:
    price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
    print(price)
    time.sleep(1)