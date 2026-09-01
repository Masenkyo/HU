import time
from machine import Pin

led = Pin(20, Pin.OUT)
switchPin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    if switchPin.value():
        led.value(1)
    else:
        led.value(0)
        time.sleep(0.1)