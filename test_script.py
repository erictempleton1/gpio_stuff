#!/usr/bin/python
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

# (relay number, gpio pin)
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

for relay_num, gpio_pin in gpio_map:
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.HIGH)

for relay_num, gpio_pin in gpio_map:
    print "relay:", relay_num, "gpio: ", gpio_pin
    GPIO.output(gpio_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(gpio_pin, GPIO.HIGH)
    time.sleep(0.1)
    time.sleep(1)

GPIO.cleanup()
