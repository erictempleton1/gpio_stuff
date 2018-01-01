#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 06     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

# gpio_list = [06, 13, 19, 26, 12, 16, 20, 21]

gpio_map = [
    ("01", 06), 
    ("02", 13), 
    ("03", 19), 
    ("04", 26), 
    ("05", 12), 
    ("06", 16), 
    ("07", 20), 
    ("08", 21)
]

for relay_num, gpio_pin in gpio_list:
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.HIGH)

for relay_num, gpio_pin in gpio_list:
    print "relay:", relay_num, "gpio: ", gpio_pin
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(gpio_pin, GPIO.HIGH)
    time.sleep(0.1)
    time.sleep(1)

GPIO.cleanup()
