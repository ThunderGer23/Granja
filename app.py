from machine import Pin
import time

p = Pin(2, Pin.OUT)

def toggle(max,t=1):
    lap = 0

    while lap < max:
        p.value(1)
        time.sleep(t)
        p.value(0)
        time.sleep(t)
        lap += 1

toggle(10,.5)