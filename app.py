from machine import Pin, PWM, Timer
from time import sleep_ms

def calperiod(grad):
    return (grad * 100)/10800

p = Pin(2, Pin.OUT)

frecuency = 500
duty = 0
dutyOff = 1023
pwm12 = PWM(Pin(12))
pwm12 = PWM(Pin(13))
pwm12 = PWM(Pin(14))

pwm12.freq(frecuency)
pwm12.duty(dutyOff)

#variables
motor = 1
grad = 35
period1 = calperiod(grad)
period2 = calperiod(grad)
period3 = calperiod(grad)
period4 = calperiod(grad)
period5 = calperiod(grad)


#set timer
tim1 = Timer(1)
tim2 = Timer(1)
tim3 = Timer(1)
p.value(1)
tim1.init(period=period, mode=Timer.PERIODIC, callback=lambda t:setLed())

def setLed():

    duty -= 10
    sleep_ms(3)
    if duty < 0:
        duty = dutyOff
        motor += 1
        if motor > 3:
            motor = 1

    if motor == 1:
        pwm12.duty(dutyOff)
    p.value(0)