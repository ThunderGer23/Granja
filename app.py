from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_0DB)
adc.atten(ADC.WIDTH_12BIT)

def readSense():
    stop = 0
    while True:
        readVal = adc.read() * 0.000855
        stop += 1
        print(readVal)
        if ( stop >= 35):
            break
        sleep(1)
    print('End test')

readSense()
