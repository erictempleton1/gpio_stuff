#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

gpio_list = [26, 19, 13, 06, 12, 16, 20, 21]

for i in gpio_list:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleep_time_short = 0.2
sleep_time_long = 0.1

# MAIN LOOP =====
# ===============

try:
    for i in gpio_list:
        GPIO.output(i, GPIO.LOW)
        time.sleep(sleep_time_short)
        GPIO.output(i, GPIO.HIGH)
        time.sleep(sleep_time_long)
        time.sleep(2)
except KeyboardInterrupt:
    print "Ending and cleaning up.."

    # Reset GPIO settings
    GPIO.cleanup()
    print "Done."