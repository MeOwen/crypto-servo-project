https://raspberrytips.com/raspberry-pi-gpio-pins/
https://gpiozero.readthedocs.io/en/stable/installing.html
https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-the-pin-factory
https://gist.github.com/tstellanova/8b1fb350a148eace6541b5fbd2c021ca

### install

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

see development install guide:
https://gpiozero.readthedocs.io/en/stable/development.html

1. sudo apt install lsb-release build-essential git exuberant-ctags \
    virtualenvwrapper python-virtualenv python3-virtualenv \
    python-dev python3-dev pigpio
2. sudo systemctl start pigpiod
3. cd crypto-servo-project/
4. mkvirtualenv -p /usr/bin/python3 crypto-servo
5. pip3 install -r requirements.txt

## commands
- pinout
- sudo service pigpiod status

### virtualenvwrapper commands
- lsvirtualenv
- rmvirtualenv
- mkvirtualenv -p /usr/bin/python3 [projectname]
- workon [projectname]
- deactivate

## todo
stop servo on ctrl-c: https://www.devdungeon.com/content/python-catch-sigint-ctrl-c